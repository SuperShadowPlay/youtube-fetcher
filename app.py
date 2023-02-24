from fetch import fetch
import os
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog
except ImportError:
    from Tkinter import *
    from Tkinter import filedialog
    import ttk

class App:

    def __init__(self, main_root):
        self.root = main_root

        # Window title
        self.root.title('YouTube Fetcher')

        # Variables
        self.folder_path = StringVar()
        self.codec = StringVar()
        self.status_message = StringVar()
        self.extra_options = StringVar()
        self.file_numbering = StringVar()

        self.ENTRY_BOX_ROW = 1
        self.CONFIG_ROW = self.ENTRY_BOX_ROW + 5
        self.PBAR_ROW = self.CONFIG_ROW + 1

        # Init everything else
        self.init_style()
        self.init_frames()
        self.init_entry()
        self.init_config()
        self.init_status_area()
        self.bind_events()


    def init_style(self):
        '''Thank you to rbende for the great premade theme! Source repo in README.md'''
        self.root.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')


    def init_frames(self):
        '''Configure root and mainframe'''
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def init_entry(self):
        '''Entry box configuration'''
        # Text entry box
        self.entry_box = Text(self.mainframe, width=70, height=10)
        self.entry_box.grid(column=1, row=self.ENTRY_BOX_ROW, columnspan=5, rowspan=3, padx=5, pady=5, sticky=(N,S,W,E))
        self.entry_box['wrap'] = 'none'
        self.entry_box.insert('1.0', 'Enter video URLs seperated by lines')


    def init_config(self):
        '''Config area init'''
        # Area seperator
        ttk.Separator(self.mainframe, orient=HORIZONTAL).grid(column=1, row=self.CONFIG_ROW - 1, columnspan=5, sticky=(N,S,W,E), pady=5)        
        
        # Init frame that contains config stuff
        self.config_frame = ttk.Frame(self.mainframe)
        self.config_frame.grid(column=1, row=self.CONFIG_ROW, sticky=(N,W,E,S), columnspan=5)
        self.config_frame.grid_columnconfigure(5,weight=1) # Allow an invisible 5th column to expand and let some widgets span multiple columns

        # Browse button
        self.browse_button = ttk.Button(self.config_frame, text='Browse', command=self.grab_folder_path)
        self.browse_button.grid(column=1, row=self.CONFIG_ROW, pady=10, padx=5, sticky=(W,E))

        # Folder select entry box
        self.folder_entry = ttk.Entry(self.config_frame, textvariable=self.folder_path)
        self.folder_entry.grid(column=2, row=self.CONFIG_ROW, sticky=(E,W), columnspan=4, padx=5, pady=5)
        self.folder_path.set('No Folder Selected')
        self.folder_entry.state(['disabled'])

        # Codec selection box
        ttk.Label(self.config_frame, text='Select audio codec:').grid(column=1, row=self.CONFIG_ROW + 1, sticky=(N,S), padx=5, pady=5)
        self.codec_select_box = ttk.Combobox(self.config_frame, textvariable=self.codec)
        self.codec_select_box.grid(column=2, row=self.CONFIG_ROW + 1, sticky=(N,S,W), padx=5, pady=5)
        self.codec_select_box['values'] = ('best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav')
        self.codec.set('m4a')
        self.codec_select_box.state(["readonly"])

        # Seperator between codec and numbering
        ttk.Separator(self.config_frame, orient=VERTICAL).grid(column=3, row=self.CONFIG_ROW + 1, sticky=(N,S,W,E), padx=5)

        # Keep video box
        self.keep_video_box = ttk.Checkbutton(self.config_frame, text='Keep Video', variable=self.extra_options,
	    onvalue='-k', offvalue='')
        self.keep_video_box.grid(column=4, row=self.CONFIG_ROW + 1, sticky=(N,S,E), padx=5, pady=5)
        self.extra_options.set('')

        # Numbering outputs
        self.numbering_checkbox = ttk.Checkbutton(self.config_frame, text='Enable Numbering', command=self.toggle_numbering)
        self.numbering_checkbox.grid(column=1, row=self.CONFIG_ROW + 2, padx=5, pady=5)
        self.number_select = ttk.Spinbox(self.config_frame, from_=1.0, to=100.0, textvariable=self.file_numbering)
        self.number_select.grid(column=2, row=self.CONFIG_ROW + 2)
        self.number_select['state'] = 'disabled'
        # THIS DOES NOTHING YET


    def init_status_area(self):
        '''Configure progress bar, go button, and status message'''
        # Go button
        self.go_button = ttk.Button(self.mainframe, text='Go!', command=self.start_fetch)
        self.go_button.grid(column=2, row=self.PBAR_ROW, sticky=(N,S,E), padx=5, pady=10, columnspan=5)

        # Status message
        status_label = ttk.Label(self.mainframe, textvariable=self.status_message)
        status_label.grid(column=1, row=self.PBAR_ROW, columnspan=4, sticky=(N,S,W), padx=5, pady=10)
        self.status_message.set('')

        # Seperator
        ttk.Separator(self.mainframe, orient=HORIZONTAL).grid(column=1, row=self.PBAR_ROW + 1, columnspan=5, sticky=(N,S,W,E), pady=5)

        # Progress bar
        self.root.update()
        window_width = self.root.winfo_width()
        self.pbar = ttk.Progressbar(self.mainframe, orient=HORIZONTAL, length=window_width, mode='determinate')
        self.pbar.grid(column=1, row=self.PBAR_ROW + 2, columnspan=5, padx=5)


    def bind_events(self):
        '''Event registration'''
        self.entry_box.focus()
        self.entry_box.tag_add('sel', '1.0', 'end')
        self.root.bind('<Escape>', lambda e: quit())
        self.codec_select_box.bind('<<ComboboxSelected>>', lambda e: self.mainframe.focus())
        

    def start_fetch(self, *args):
        '''Grab URLs and send them to the fetcher'''

        # Make sure a folder is selected
        if self.folder_path.get() == 'No Folder Selected':
            self.grab_folder_path()

        # Prep GUI for downloading
        self.entry_box['state'] = 'disabled'
        self.pbar['value'] = 0
        self.status_message.set('Fetcher is working, even if the window is not responding...')

        # Grab songs and folder path
        songs = self.entry_box.get('1.0', 'end').split('\n')
        path = self.folder_path.get()

        # Do the thing
        self.pbar['maximum'] = float(len(songs))
        self.pbar['value'] += 1
        for song in songs:
            self.root.update_idletasks()
            self.root.after(200, fetch(path, song, self.codec.get(), options=self.extra_options.get())) # pass everything over to the yt-dlp file
            self.pbar['value'] += 1

        # Set GUI back to normal state
        self.entry_box['state'] = 'normal'
        self.pbar['value'] = 0
        self.status_message.set('Done!')

    
    def grab_folder_path(self, *args):
        filename = filedialog.askdirectory()
        if filename != '':
            self.folder_path.set(filename)

    
    def toggle_numbering(self, *args):
        if self.number_select:
            pass
            # THIS DOES NOTHING

if __name__ == '__main__':
    input('You should run "main.py" instead!')

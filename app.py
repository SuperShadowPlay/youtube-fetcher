from fetch import fetch
import os
try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import *
    import ttk

class App:

    def __init__(self, main_root):
        self.root = main_root

        # Window title
        self.root.title('StudyChill Fetcher')

        # Configure root and mainframe Frame
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Variables
        self.mode = StringVar()
        self.folder_path = StringVar()

        # Init everything else
        self.init_entry_frame()
        self.init_progress_bar_frame()
        self.init_right_column_frame()
        self.bind_events()

    def init_entry_frame(self):
        '''Entry box configuration'''
        # Frame
        self.entry_frame = ttk.Frame(self.mainframe)
        self.entry_frame.grid(column=0, row=0)

        # Text entry box
        self.entry_box = Text(self.entry_frame, width=40, height=10)
        self.entry_box.grid(column=1, row=1, columnspan=5, rowspan=3, padx=5, pady=5, sticky=(N,S,W,E))
        self.entry_box['wrap'] = 'char'
        self.entry_box.insert('1.0', 'Enter video URLs')

        # Scrollbar
        ys = ttk.Scrollbar(self.entry_frame, orient=VERTICAL, command=self.entry_box.yview)
        self.entry_box['yscrollcommand'] = ys.set

    def init_progress_bar_frame(self):
        '''Configure progress bar'''
        self.root.update()
        wd = self.root.winfo_width()
        self.progress_bar_frame = ttk.Frame(self.mainframe)
        self.progress_bar_frame.grid(column=0, row=1)
        self.pbar = ttk.Progressbar(self.progress_bar_frame, orient=HORIZONTAL, length=wd, mode='determinate')
        self.pbar.grid(column=1, row=1)

    def init_right_column_frame(self):
        '''Right column configuration'''
        # Frame
        self.right_column = ttk.Frame(self.root, padding="3 12 12 0")
        self.right_column.grid(column=1, row=0, sticky=(N,W,E))

        # Misc right column
        ttk.Button(self.right_column, text='Go!', command=self.start_fetch).grid(column=1, row=5, sticky=(W,E), padx=5, pady=5)
        ttk.Label(self.right_column, text='Folder select').grid(column=1, row=1, sticky=(W,S,N), pady=5)
        
        # Right column folder select entry box
        self.folder_entry = ttk.Entry(self.right_column, textvariable=self.folder_path, text='hi'); self.folder_entry.grid(column=1, row=4)
        self.folder_entry.insert(0, './'); self.folder_path.set('./')
        self.folder_entry.state(['disabled'])

        # Right column radio buttons
        rb1 = ttk.Radiobutton(self.right_column, text='Individual', variable=self.mode, value='individual',
            command=lambda: self.configure_mode(self.folder_entry))
        rb2 = ttk.Radiobutton(self.right_column, text='Folder', variable=self.mode, value='folder',
            command=lambda: self.configure_mode(self.folder_entry))
        rb1.grid(column=1, row=2, sticky=W)
        rb2.grid(column=1, row=3, sticky=W)
        rb1.invoke()

    def bind_events(self):
        '''Event registration'''
        self.entry_box.focus()
        self.entry_box.tag_add('sel', '1.0', 'end')
        self.root.bind('<Escape>', lambda e: quit())
        self.folder_entry.bind('<FocusOut>', self.configure_mode)
        
    def start_fetch(self, *args):
        '''Grab URLs and send them to the fetcher'''
        self.entry_box['state'] = 'disabled'
        self.pbar['value'] = 0
        songs = self.entry_box.get('1.0', 'end').split('\n')
        path = self.folder_path.get()

        self.pbar['maximum'] = float(len(songs))
        self.pbar['value'] += 1
        for song in songs:
            print('Max: {}'.format(self.pbar['maximum']), 'Val: {}'.format(self.pbar['value']))
            self.root.update_idletasks()
            self.root.after(200, fetch(path, song, 'mp3'))
            self.pbar['value'] += 1

        self.entry_box['state'] = 'normal'


    def configure_mode(self, *args):
        '''Called when radio buttons are clicked on and when folder location is updated.'''
        if self.mode.get() == 'folder':
            self.folder_entry.state(['!disabled'])
        else:
            self.folder_entry.state(['disabled'])

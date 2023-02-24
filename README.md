# YouTube Fetcher

I find myself grabbing mp3s off of youtube a lot, so I made a small
app that makes the process a bit easier on myself.
This program is essentially just a `yt-dlp` GUI specialized for how I use `yt-dlp`.

Is it janky? Yes!

Does it work? Mostly!

# How to run

`$ python main.py`

Or if your operating system allows, just open `main.py` from your file browser.

If you need to install yt-dlp and are scared of a command prompt, simply run the `setup.py` file to install it automatically.

# Acknowledgement

Thank you to [rbende](https://github.com/rdbende) for making the [great theme](https://github.com/rdbende/Forest-ttk-theme) used in this program.

## Future Features

- [x] Make folder selection work
- [x] Allow user to specify audio codec
- [ ] Ask user to install `yt-dlp` if not found
- [ ] Properly integrate `yt-dlp`
- [ ] Option to automatically number downloads
- [x] Allow video downloads
- [ ] Allow thumbnail image downloads
- [ ] More intuitive way to enter URLs
- [x] Give the app a nice theme
- [ ] Make config choices persistent over multiple sessions
- [ ] Parallel downloaders
- [ ] Add a nice "About" button

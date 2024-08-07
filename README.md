# YouTube Fetcher

I find myself grabbing mp3s off of youtube a lot, so I made a small
app that makes the process a bit easier on myself.
This program is essentially just a `yt-dlp` GUI specialized for how I use `yt-dlp`.
It's a simple script, but it's honest code.

Is it janky? Yes!

Does it work? Mostly!

![App Screenshot](./src/App_Screenshot.png)

# How to run

`$ python main.py`

Or if your operating system allows, just open `main.py` from your file browser.

If you need to install yt-dlp and are scared of a command prompt, simply run the `setup.py` file to install it automatically.

## Future Features

- [x] Make folder selection work
- [x] Allow user to specify audio codec
- [ ] Ask user to install `yt-dlp` if not found
- [ ] Properly integrate `yt-dlp`
- [ ] Option to automatically number downloads
- [x] Allow video downloads
- [ ] Allow thumbnail downloads
- [ ] More intuitive way to enter URLs
- [ ] Give the app a nice theme
- [ ] Make config choices persistent over multiple sessions
- [ ] Organize files for distribution on pypi

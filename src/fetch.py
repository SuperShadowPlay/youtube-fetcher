from os import system

def fetch(path, songURL, audio_format, options=''):
    if 'youtu' in songURL:
        print(' -> Downloading url {0}'.format(songURL))
        command = 'yt-dlp -o {0}/%(title)s-%(uploader)s.%(ext)s -x --audio-format {1} --add-metadata --cookies-from-browser firefox --embed-thumbnail {2} {3}'.format(
            path, audio_format, songURL, options)
        system(command)        
    else:
        if songURL == '':
            pass # Ignore spurrious newlines
        else:
            print(f'Problem parsing URL "{songURL}"')
            pass


if __name__ == "__main__":
    # Run as a shell script
    from sys import argv

    if len(argv) in (3, 4): # Correct amount of args
        fmt = argv[3] if len(argv) == 4 else "m4a"
        fetch(argv[2], argv[1], fmt)
    else:
        print("Incorrect Usage: python fetch.py <songURL> <path output> [optional format]")
        

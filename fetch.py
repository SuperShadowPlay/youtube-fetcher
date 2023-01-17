from os import system

def fetch(path, songURL, audio_format, options=''):
    if 'youtu' in songURL:
        print(' -> Downloading url {0}'.format(songURL))
        command = 'yt-dlp -o {0}/%(title)s-%(uploader)s.%(ext)s -x --audio-format {1} --add-metadata --embed-thumbnail {2} {3}'.format(
            path, audio_format, songURL, options)
        system(command)        
    else:
        if songURL == '':
            pass # Ignore spurrious newlines
        else:
            print(f'Problem parsing URL "{songURL}"')
            pass

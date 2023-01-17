'''Essentially just runs the command to install yt-dlp for people who don't like the commandline.'''
from os import system
from time import sleep

command = 'python -m pip install yt-dlp --user -U'
system(command)
print('\nDone!')
sleep(5)
#yt2mp3 is a python executable that allows a user to type in two fields:
#File Name - the semantic file name of the audio file you would like to create
#YT Link - the full link to the youtube video you would like to grab the mp3 stream from
#This was not intended to violate copyright - any violations of copyright are the responsibility of the user
#dependencies - kivy, pytube, ffmpeg installed on computer and in env var PATH

from pytube import YouTube

import subprocess

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size=(400,300)

from functools import partial

import os
import sys


#declare app
class yt2mp3(App):
    def build(self):
        f = GridLayout(cols=1, padding=50)

        self.fnameLabel = Label(text='File Name')
        f.add_widget(self.fnameLabel)
        
        #filename text input
        self.filename = TextInput(multiline=False)
        f.add_widget(self.filename)

        #yt link label
        self.linkLabel = Label(text='YT Link')
        f.add_widget(self.linkLabel)

        #yt link text input
        self.link = TextInput(multiline=False)
        f.add_widget(self.link)

        #dl button
        self.dlButton = Button(text='Download')
        self.dlButton.bind(on_press=partial(self.dl, self))
        f.add_widget(self.dlButton)

        return f

    #download button 'onclick' logic
    def dl(self, *args, **kwargs):

            #print text input values
            filename = args[0].filename.text
            link = args[0].link.text

            # creating YouTube object
            yt = YouTube(link) 

            # accessing audio streams of YouTube obj (highest bitrate audio stream is typically last)
            stream = yt.streams.filter(only_audio=True, mime_type='audio/webm', abr='160kbps').last()

            #DEBUG
            print(stream)

            # download into working directory
            print(stream.download(filename=filename+'.webm'))
            
            #convert webm version of newly downloaded file to mp3
            #could be run conditionally with a different filename if text input is left blank
            print(subprocess.run(["ffmpeg", "-i", f"{filename}.webm", "-vn", "-ab", "320k", "-ar", "44100", "-y", f"{filename}.mp3"], capture_output=True, shell=True))

            #delete old webm file as mp3 file now exists, and the webm file is basically clutter
            #could be conditionally removed based on a radio button or checkbox 
            print(os.remove(f"{filename}.webm"))

#run app
if __name__ == '__main__':
    yt2mp3().run()
    


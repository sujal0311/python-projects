import moviepy.editor
from tkinter.filedialog import *

vid=askopenfilename()
video=moviepy.editor.VideoFileClip(vid)
filename=input("Enter audio file name with .mp3 : ")
aud=video.audio
aud.write_audiofile(filename)

print("---END---")
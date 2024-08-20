#pip install playsound --break-system-packages

from gtts import gTTS
import playsound
import os

text = gTTS(text='oh my gotto what are you doing man',lang="en",slow=False)
text.save("sound.mp4")
playsound.playsound("sound.mp4",True)
os.remove("sound.mp4")

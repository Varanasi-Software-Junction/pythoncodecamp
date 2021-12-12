from playsound import playsound
from gtts import gTTS
import os
import random as rnd
mytext = "Ba ba black sheep have you any tea "
filename = str(int(100000 * rnd.random())) + ".mp3"
language = 'en'
try:
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    playsound(filename)
    os.remove(filename)
except:
    pass

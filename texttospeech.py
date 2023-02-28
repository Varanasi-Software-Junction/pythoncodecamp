from playsound import playsound
from gtts import gTTS
import os
import random as rnd
mytext = """टीचर- Aman ji इतने दिन कहां थे, स्कूल क्यों नहीं आए?

Aman- बर्ड फ्लू हो गया था मैम।

टीचर- पर ये तो पक्षियों को होता है इंसानों को नहीं।

Aman- इंसान समझा ही कहां आपने...रोज तो मुर्गा बना देती हो..!! """
filename = str(int(100000 * rnd.random())) + ".mp3"
language = 'en'
try:
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    playsound(filename)
    os.remove(filename)
except:
    pass

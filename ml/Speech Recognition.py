import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Say something...")
    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)
    # Listen for audio input
    audio = r.listen(source)

# Use Google's speech recognition service to convert audio to text
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Unable to recognize speech")
except sr.RequestError as e:
    print(f"Error: {e}")

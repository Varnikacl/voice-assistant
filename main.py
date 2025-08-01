import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hi! Speak something"); engine.runAndWait()
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    cmd = r.recognize_google(audio)
    print("You said:", cmd)
    engine.say(f"You said {cmd}"); engine.runAndWait()
except Exception as e:
    print("Error:", e)
    engine.say("Sorry, I didn't catch that."); engine.runAndWait()
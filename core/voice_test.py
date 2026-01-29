import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("🧠 You said:", text)
except sr.UnknownValueError:
    print("❌ Sorry, I could not understand the audio")
except sr.RequestError as e:
    print("❌ Could not request results; {0}".format(e))

import speech_recognition as sr

WAKE_WORD = "friday"

recognizer = sr.Recognizer()
microphone = sr.Microphone()

print("🟡 VAJRA is idle. Say 'Friday' to wake me up.")

while True:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        speech_text = recognizer.recognize_google(audio).lower()
        print("👂 Heard:", speech_text)

        if WAKE_WORD in speech_text:
            print("🟢 Wake word detected! VAJRA is awake.")
            break
        else:
            print("⚪ Wake word not detected. Staying idle.")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ Speech service error: {e}")

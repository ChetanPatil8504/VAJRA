from action_executor import execute_action
from intent_parser import extract_intent
import speech_recognition as sr

WAKE_WORD = "friday"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.6
recognizer.dynamic_energy_threshold = True

microphone = sr.Microphone()
print("🔧 Calibrating microphone, please stay silent...")
with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
print("✅ Calibration complete.")


def listen_and_recognize(prompt_text):
    with microphone as source:
        print(prompt_text)
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

print("🟡 VAJRA is idle. Say 'Friday' to wake me up.")

# ---- WAKE LISTEN LOOP ----
while True:
    speech = listen_and_recognize("🎤 Listening for wake word...")
    if WAKE_WORD in speech:
        print("🟢 Wake word detected. VAJRA is awake.")
        break
    else:
        print("⚪ Wake word not detected.")

# ---- COMMAND LISTEN ----
command = listen_and_recognize("🎧 Listening for your command...")

if command:
    intent_data = extract_intent(command)
    print("🧠 Command:", command)
    print("🎯 Intent:", intent_data)
    execute_action(intent_data)
else:
    print("❌ No command detected.")

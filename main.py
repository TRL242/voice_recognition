import speech_recognition
import pyttsx3
import pyaudio

recognizer = speech_recognition.Recognizer()

while True:
    
    try:
        
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            with open("voice_recording.txt", "w") as file:
                file.write(text)

            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue

            
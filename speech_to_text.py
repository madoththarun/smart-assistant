import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    
    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)  # Listen for audio

    try:
        # Use Google Web Speech API to recognize the audio
        voice_data = r.recognize_google(audio)
        print(voice_data)  # Optional: print recognized text for debugging
        return voice_data  # Return the recognized text
    except sr.UnknownValueError:
        print("Could not understand audio")  # Print an error message if audio is unclear
        return ""  # Return an empty string on failure
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")  # Print specific error
        return ""  # Return an empty string on request error

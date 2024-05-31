import speech_recognition as sr

def capture_voice_input(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return text

def process_voice_command(text):
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "you look good today" in text.lower():
        print("Thank you! You're so kind!")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    else:
        print("I didn't understand that command. Please try again.")
    return False

def main():
    recognizer = sr.Recognizer()
    end_program = False
    while not end_program:
        try:
            audio = capture_voice_input(recognizer)
            text = convert_voice_to_text(recognizer, audio)
            end_program = process_voice_command(text)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

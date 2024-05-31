import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from datetime import datetime


def capture_voice_input(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio


def convert_voice_to_text(recognizer, audio, language):
    try:
        text = recognizer.recognize_google(audio, language=language)
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
        response = "Hello, How can I help you?"
    elif "你今天看起来很好" in text:  # "You look good today" in Mandarin
        response = "谢谢！你太好了！"  # "Thank you! You're so kind!" in Mandarin
    elif "anda kelihatan baik hari ini" in text.lower():  # "You look good today" in Malay
        response = "Terima kasih! Anda sangat baik!"  # "Thank you! You're so kind!" in Malay
    elif "goodbye" in text.lower() or "再见" in text or "selamat tinggal" in text.lower():
        response = "Goodbye! Have a great day!"
        return response, True
    else:
        response = "I didn't understand that command. Please try again."
    return response, False


def start_listening():
    recognizer = sr.Recognizer()
    selected_language = language_var.get()
    language_map = {"English": "en-US", "Mandarin": "zh-CN", "Malay": "ms-MY"}
    language = language_map.get(selected_language, "en-US")

    try:
        audio = capture_voice_input(recognizer)
        text = convert_voice_to_text(recognizer, audio, language)
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        text_output.set(f"You said: {text}")
        response, end_program = process_voice_command(text)
        response_output.set(f"Response: {response}\nDetected at: {current_time}")

        if end_program:
            root.quit()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Voice Command")

# Set the window size
window_width = 500
window_height = 300

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center position
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the geometry of the window
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Define StringVar to hold the text and response
text_output = tk.StringVar()
response_output = tk.StringVar()
language_var = tk.StringVar(value="English")

# Create and pack the dropdown menu for language selection
language_label = tk.Label(root, text="Select Language:")
language_label.pack(pady=5)

language_menu = tk.OptionMenu(root, language_var, "English", "Mandarin", "Malay")
language_menu.pack(pady=5)

# Create and pack the button
listen_button = tk.Button(root, text="Start Listening", command=start_listening)
listen_button.pack(pady=20)

# Create and pack the labels to display text and response
text_label = tk.Label(root, textvariable=text_output)
text_label.pack(pady=5)

response_label = tk.Label(root, textvariable=response_output)
response_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

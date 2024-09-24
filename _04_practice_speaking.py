import os
from pykakasi import kakasi
import warnings
import tkinter as tk
from tkinter import scrolledtext

warnings.filterwarnings("ignore", category=DeprecationWarning)

kks = kakasi()
kks.setMode("J", "H")  # Japanese to Kana
conv = kks.getConverter()

def speak(voice_file):
    if not os.path.exists(voice_file):
        print(f"You have navigated outside the conversation dialog. Please try again")
        return

    if os.name == 'nt':  # For Windows
        os.system(f'start {voice_file}')
    elif os.name == 'posix':  # For MacOS and Linux
        if os.uname().sysname == 'Darwin':  # MacOS
            os.system(f'afplay {voice_file}')
        else:  # Linux
            os.system(f'ffplay -nodisp -autoexit {voice_file}')

def divide_list(lst, delimiter):
    try:
        # Find the index of the delimiter
        idx = lst.index(delimiter)
        # Slice the list into two parts based on the index of the delimiter
        return lst[:idx], lst[idx+1:]
    except ValueError:
        # If the delimiter is not in the list, return the original list and an empty list
        return lst, []

with open('conversation_scripts.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

lst = lines
delimiter = '*****\n'
en_conv, ja_conv = divide_list(lst, delimiter)

num = 0

def update_text(widget, text):
    widget.config(state=tk.NORMAL)
    widget.delete('1.0', tk.END)
    widget.insert(tk.INSERT, text)
    widget.config(state=tk.DISABLED)

def clear_japanese_texts():
    update_text(japanese_text, '')
    update_text(kana_text, '')

def speak_text_en(seq):
    try:
        update_text(english_text, en_conv[seq])
        root.update()  # Ensure the GUI updates before speaking
        speak(voice_file=f'openai_en_voice_{seq}.mp3')
    except IndexError:
        print("Index out of range. Please try again.")

def speak_text_ja(seq):
    try:
        update_text(japanese_text, ja_conv[seq])
        kana = conv.do(ja_conv[seq])
        update_text(kana_text, 'Kana: {}'.format(kana))
        root.update()  # Ensure the GUI updates before speaking
        speak(voice_file=f'elevenlab_ja_voice_{seq}.mp3')
    except IndexError:
        print("Index out of range. Please try again.")


def go_forward():
    global num
    num += 1
    clear_japanese_texts()  # Clear Japanese text boxes when 'Next' is clicked
    speak_text_en(seq=num)

def go_back():
    global num
    num -= 1
    speak_text_en(seq=num)

def end_program():
    root.destroy()

def japanese():
    global num
    speak_text_ja(seq=num)

def helper():
    help_text = '''
    *********************************************
    press the "Play English" button to start or play English speech
    press the "Next" button to proceed
    press the "Previous" button to go back
    press the "Quit" button to end the program
    press the "Play Japanese" button to play Japanese speech with text
    *********************************************
    '''
    print(help_text)

def english():
    global num
    speak_text_en(seq=num)

# GUI setup
root = tk.Tk()
root.title("Japanese Conversation Practice")

# Text areas for displaying conversation
english_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=80, height=5)
english_text.pack()

japanese_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=80, height=5)
japanese_text.pack()

kana_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=80, height=5)
kana_text.pack()

# Adding buttons
btn_english = tk.Button(root, text="Play English", command=english)
btn_english.pack()

btn_next = tk.Button(root, text="Next", command=go_forward)
btn_next.pack()

btn_previous = tk.Button(root, text="Previous", command=go_back)
btn_previous.pack()

btn_japanese = tk.Button(root, text="Play Japanese", command=japanese)
btn_japanese.pack()

btn_quit = tk.Button(root, text="Quit", command=end_program)
btn_quit.pack()

helper()
root.mainloop()

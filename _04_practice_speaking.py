import os
from googletrans import Translator
from pykakasi import kakasi
from time import sleep
import keyboard
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


translator = Translator()
kks = kakasi()
kks.setMode("J", "H")  # Japanese to Kana
conv = kks.getConverter()


def speak(voice_file):
    if not os.path.exists(voice_file):
        print(f"You have navigated outside the conversation dialog. Please try again")
        return

    if os.name == 'nt':  # For Windows
        os.system(f'start {voice_file}')
    else:  # For MacOS
        os.system(f'afplay {voice_file}')


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
cont = True


def speak_text_en(seq):
    try:
        print(en_conv[seq])
        speak(voice_file=f'openai_en_voice_{seq}.mp3')
    except IndexError:
        print("Index out of range. Please try again.")

def speak_text_ja(seq):
    try:
        print(ja_conv[seq])
        kana = conv.do(ja_conv[seq])
        print('Kana: {}'.format(kana))
        speak(voice_file=f'elevenlab_ja_voice_{seq}.mp3')
    except IndexError:
        print("Index out of range. Please try again.")


def speak_text_ja_without_text(seq):
    speak(voice_file=f'elevenlab_ja_voice_{seq}.mp3')


def go_forward(e):
    global num
    num += 1
    speak_text_en(seq=num)


def go_back(e):
    global num
    num -= 1
    speak_text_en(seq=num)


def repeat(e):
    global num
    speak_text_ja_without_text(seq=num)


def end_program(e):
    global cont
    cont = False


def japanese(e):
    global num
    speak_text_ja(seq=num)


def helper(e):
    print('''
    *********************************************
    press enter to start or play English speech
    press   >   to proceed
    press   <   to go back
    press  esc  to end the program
    press space to play Japanese speech with text
    press   ^   to repeat Japanese speech  
    press  tab   for help
    *********************************************
    ''')


def english(e):
    global num
    speak_text_en(seq=num)


keyboard.on_press_key('enter', english)
keyboard.on_press_key('left', go_back)
keyboard.on_press_key('right', go_forward)
keyboard.on_press_key('esc', end_program)
keyboard.on_press_key('up', repeat)
keyboard.on_press_key('space', japanese)
keyboard.on_press_key('tab', helper)

helper('')
while cont:
    pass

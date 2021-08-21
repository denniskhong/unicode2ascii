#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

""" 
    Name:        Unicode to ASCII converter
    Filename:    u2a.py
    Description: Python program to convert Unicode characters to ASCII characters in clipboard
    Author:      Dennis Khong
    Email:       denniswkkhong@gmail.com
    Version:     1.0
    Date:        21 August 2021
    Repository:  https://github.com/denniskhong/unicode2ascii

    The xclip library is needed in Linux:
    apt install xclip
"""

import pyperclip     # To access the clipboard for copy and paste
from unidecode import unidecode
import tkinter as tk

# Variable initialisation
text_ascii = ''

window = tk.Tk()
window.title('Unicode to ASCII Converter')

def onclick():
    text_ascii = unidecode(pyperclip.paste())
    pyperclip.copy(text_ascii)
    
    textbox.config(state='normal')
    textbox.delete(1.0, 'end')
    textbox.insert('end', text_ascii)
    textbox.config(state='disabled')
    
button = tk.Button(window, text='Paste & Convert', font='sans 12 bold', command=onclick).pack(side='top', anchor='n')

label = tk.Label(window, text='Clipboard:', font='sans 12 bold').pack(side='top', anchor='w')

textbox = tk.Text(window, width=80, height=20, wrap='word', font=('Arial', 14))
textbox.pack(expand=True, fill='both')
textbox.insert('end', '')
textbox.config(state='disabled')

window.mainloop()



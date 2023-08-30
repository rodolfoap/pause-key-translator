#!/bin/env python3
from pynput import keyboard # Requires: pip install pynput
import clipboard # Requires: pip install clipboard
import pyautogui # Requires: pip install pyautogui
from subprocess import check_output

TRANSLATION="es:fr"

class Translator:
	def __init__(this):
		with keyboard.Listener(on_press=this.on_press) as listener: listener.join()
	def on_press(this, key):
		if key==keyboard.Key.pause:
			pyautogui.hotkey('ctrl', 'c') # Copies selection to clipboard using CTRL-C
			text=clipboard.paste()        # Puts copied text into a variable
			print('Original  :', text)
			with open('/tmp/text', 'w') as f: f.write(text)
			text=check_output(["/usr/local/bin/trans", "-b", "-i", "/tmp/text", TRANSLATION]).decode("utf-8")
			print('Translated:', text)
			clipboard.copy(text)          # Puts text into the clipboard
			pyautogui.hotkey("ctrl", "v") # Pastes selection from clipboard using CTRL-V
Translator()

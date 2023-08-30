# pause-key-translator

Simple app allowing translation using the PAUSE key

## Install
```
cp trans pause-key-translator.py /usr/local/bin/
```

## Usage

1. Define the TRANSLATION variable in `/usr/local/bin/pause-key-translator.py`.
2. Launch the application: `pause-key-translator.py`
3. Open **libreoffice** or any graphical editor (must be graphical mode, because CTRL-C is used; if you use **vim**, you should hack the COPY and PASTE values in the python script).
4. Select some text in the original language.
5. Press the PAUSE key. The translated text will replace the original. Notice that the clipboard contains the translation now.

## Notes

Translate-shell (`trans`) is the default build of https://github.com/soimort/translate-shell/releases/tag/v0.9.7.1

# pause-key-translator

Simple app allowing translation using the PAUSE key

## Install
```
cp trans pause-key-translator.py /usr/local/bin/
```

## Usage

1. Define the TRANSLATION variable in `/usr/local/bin/pause-key-translator.py`.
2. Open **libreoffice** or any graphical editor (must be graphical mode, because CTRL-C is used; if you use **vim**, you should hack the COPY and PASTE values in the python script.
3. Select some text in the original language.
4. Press the PAUSE key. The translated text will replace the original

## Notes

Translate-shell (`trans`) is the default build of https://github.com/soimort/translate-shell/releases/tag/v0.9.7.1

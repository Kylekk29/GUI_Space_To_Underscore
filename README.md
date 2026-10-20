**English** | [简体中文](README.zh-CN.md)

# GUI Space to Underscore

A tiny window that turns text like `my file name: v2` into `my_file_name__v2`. Spaces and colons become underscores, and the result goes straight to your clipboard.

## Features

- Replaces **spaces** and **colons** with `_`
- Two ways in: take the text already on your clipboard, or type it in
- The result is copied to the clipboard, ready to paste
- Fixed 500×500 window

## Usage

1. Run the script.
2. Click **Clipboard** to convert whatever you copied, or type text in the box and click **Submit**.
3. Paste the result anywhere.

## Run from source

Python 3. Tkinter is included with Python; `pyperclip` is the only extra.

```bash
pip install -r requirements.txt
python GUI_space_to_underscore.py
```

## License

MIT, see [LICENSE](LICENSE).

[English](README.md) | **简体中文**

# GUI Space to Underscore（空格转下划线）

一个很小的窗口工具，把 `my file name: v2` 这样的文字变成 `my_file_name__v2`。空格和冒号都会变成下划线，结果直接复制到剪贴板。

## 功能

- 把**空格**和**冒号**替换为 `_`
- 两种输入方式：读取剪贴板里已有的文字，或手动输入
- 结果自动复制到剪贴板，可直接粘贴
- 固定 500×500 的窗口

## 使用方法

1. 运行脚本。
2. 点击 **Clipboard** 转换你刚复制的内容，或在输入框中输入文字后点击 **Submit**。
3. 把结果粘贴到任何地方。

## 从源码运行

需要 Python 3。Tkinter 随 Python 自带，唯一额外需要的是 `pyperclip`。

```bash
pip install -r requirements.txt
python GUI_space_to_underscore.py
```

## 许可证

MIT，见 [LICENSE](LICENSE)。

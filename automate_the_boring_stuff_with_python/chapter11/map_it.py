import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #剪切板内容
#webbrowser.open('https://www.amap.com/' + address)
webbrowser.open('http://www.qq.com/')
import sys, requests, pyperclip, webbrowser, bs4

if len(sys.argv) > 0:
    param = ' '.join(sys.argv[1:])
else:
    param = pyperclip.paste()
param = 'python'
print("param = %s" %(param))

#webbrowser.open(""+param)
#百度搜索格式   https://www.baidu.com/s?wd=%E4%B8%8A%E6%B5%B7
base_url = 'http://www.runoob.com'
res = requests.get(base_url + "/python/python-tutorial.html")
try:
    res.raise_for_status()
except Exception as exc:
    print('There is a problem %s'% (exc))

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select('#leftcolumn a')
for i in range(3):
    webbrowser.open(base_url + linkElems[i]['href'])
print(len(linkElems))
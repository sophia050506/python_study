import re
phone_regex = re.compile(r'''(
(\d{3})?
(\s|-|\.)?
(\d{4})
(\s|-|\.)?
(\d{4})
)''', re.VERBOSE)

mail_regex = re.compile(r'''(
[a-zA-z0-9+_\-%.]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-z]{2,4})
)''', re.VERBOSE)

#num = input('Enter the phone number :')
num = "123-1212-2121"
print(phone_regex.findall(num))
#email = input('Enter the email :')
email = "232346543221134@qq.com"
print(mail_regex.findall(email))

lin = re.compile(r'([a-z]{1,}){8,}')
print(lin.findall("azqazazxsdsx"))
s = " buujas "
def strip(s, cha=''):
    regex = re.compile(cha)
    print(regex.findall(s))

strip(s)

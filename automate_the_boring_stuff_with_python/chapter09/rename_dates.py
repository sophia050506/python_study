import shutil, os, re

#美国风格 MM-DD-YYYY
#欧洲风格 DD-MM-YYYY

#美国日期风格正则
global amer_date_pattern, euro_date_pattern, zero_patter
amer_date_pattern = re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
''', re.VERBOSE)

euro_date_pattern = re.compile(r'^(.*?)((0|1|2|3)?\d)-((0|1)?\d)-((19|20)?\d\d)(.*?)$')

zero_patter = re.compile(r'^(.*?)(0)?(\d)+(.*?)$')
#便利文件夹

def amer_date_to_euro_date():
    for file_name in os.listdir():
        print("文件名:",file_name)
        mo = amer_date_pattern.search(file_name)
        if mo == None:
            continue
        before_part = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        after_part = mo.group(8)

        euro_file_name = before_part + day + '-' + month + '-' + year + after_part
        abs_file_path = os.path.abspath('.')
        print("欧标文件名：",euro_file_name,"\n文件路径：",abs_file_path)

        file_name = os.path.join(abs_file_path, file_name)
        euro_file_name = os.path.join(abs_file_path, euro_file_name)

        shutil.move(file_name, euro_file_name)
        print("rename %s to $ %s" %(file_name, euro_file_name))

def euro_date_to_amer_date():
    for file_name in os.listdir():
        print("文件名:",file_name)
        mo = euro_date_pattern.search(file_name)
        if mo == None:
            continue
        before_part = mo.group(1)
        day = mo.group(2)
        month = mo.group(4)
        year = mo.group(6)
        after_part = mo.group(8)

        amer_file_name = before_part + month + '-' + day + '-' + year + after_part
        abs_file_path = os.path.abspath('.')
        print("美标文件名：",amer_file_name,"\n文件路径：",abs_file_path)

        file_name = os.path.join(abs_file_path, file_name)
        euro_file_name = os.path.join(abs_file_path, amer_file_name)

        shutil.move(file_name, amer_file_name)
        print("rename %s to $ %s" %(file_name, amer_file_name))


def add_befor():
    for file_name in os.listdir():
        print(type(file_name))
        after_file_name = "spam_" + file_name
        print(after_file_name)
        #shutil.move(file_name, after_file_name)

def remove_zero():
    for file_name in os.listdir():
        print(file_name)
        mo = zero_patter.search(file_name)
        if mo == None:
            continue
        befor_part = mo.group(1)
        num = mo.group(3)
        end_part = mo.group(4)
        new_file_name = befor_part + num + end_part
        print("rename %s to %s "%(file_name, new_file_name))
        #添加romove




#amer_date_to_euro_date()
#euro_date_to_amer_date()
#add_befor()
remove_zero()
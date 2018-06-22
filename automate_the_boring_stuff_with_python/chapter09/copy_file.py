import os, shutil, logging
logging.basicConfig(level=logging.DEBUG,format ='%(asctime)s-%(levelname)s-%(message)s')

logging.debug("begin")
def copy_file(folder):
    for folder_name, subfolders, file_names in os.walk(folder):
        #print("folder_name = %s, subfolders = %s, file_names = %s" % (folder_name, subfolders, file_names))
        #print(folder_name)
        logging.info(folder_name)
        for file_name in file_names:
            if file_name.endswith('.txt'):
                print(folder_name +"\\"+ file_name)
                print(os.path.abspath(".") + "\\copy\\" + file_name)
                shutil.copyfile(folder_name +"\\"+ file_name, os.path.abspath(".")+"\\copy\\"+file_name)
#copy_file("/home/sophia/PycharmProjects/python_study/automate_the_boring_stuff_with_python")
#copy_file("E:\\pythonDemo\\python_study\\automate_the_boring_stuff_with_python")
#print("hello".lower() == "Hello".lower())

s = '{"1000":"水电煤", "2000":"手机充值", "9100":"车主服务", "6001":"教育/党费缴纳", "5001":"交通罚款","9200":"物业缴费", "7001":"优选车险", "7002":"个资安全险", "7003":"女性疾病险", "7004":"监护责任险", "7005":"机票", "7006":"留学缴费", "7007":"海关税费","7008":"旅游", "7009":"惠民生活", "7010":"全民购"}'
print(len(s))
import os, shutil, logging
logging.basicConfig(level=logging.DEBUG,format ='%(asctime)s-%(levelname)s-%(message)s')

logging.debug("begin")
def copy_file(folder):
    for folder_name, subfolders, file_names in os.walk(folder):
        #print("folder_name = %s, subfolders = %s, file_names = %s" % (folder_name, subfolders, file_names))
        print(folder_name)
        logging.info(folder_name)
        for file_name in file_names:
            if file_name.endswith('.txt'):
                print(folder_name +"/"+ file_name)
                print(os.path.abspath(".") + "/copy/" + file_name)
                #shutil.copy(folder_name +"/"+ file_name, os.path.abspath(".")+"/copy")
#copy_file("/home/sophia/PycharmProjects/python_study/automate_the_boring_stuff_with_python")
print("hello".lower() == "Hello".lower())
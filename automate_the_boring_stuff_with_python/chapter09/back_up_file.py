import zipfile, os
def backup_to_zip(folder):
    number = 1
    while True:
        zipfile_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        print(zipfile_name)
        if not os.path.exists(zipfile_name):
            break
        number += 1

        backup_zip = zipfile.ZipFile(zipfile_name, 'w')
        for folder_name, subfolders, file_names in os.walk(folder):
            print("folder_name = %s, subfolders = %s, file_names = %s" % (folder_name, subfolders, file_names))
            print("Add file in %s..."%(folder_name))
            backup_zip.write(folder_name)

            for file_name in file_names:
                new_base = os.path.basename(folder) + '-'
                if file_name.startswith(new_base) and file_name.endswith('.zip'):
                    continue
                backup_zip.write(os.path.join(folder_name, file_name))
        backup_zip.close()
        print("Done!")


backup_to_zip("/home/sophia/PycharmProjects/python_study/automate_the_boring_stuff_with_python")

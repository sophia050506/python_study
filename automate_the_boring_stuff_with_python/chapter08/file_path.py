import os
import shelve
import pprint
print(os.getcwd())
print(os.path.relpath('/home/sophia','/home/sophia/PycharmProjects'))

file = open(os.getcwd()+"/bacon.txt", 'w')
file.write("Hello world!\n")
file.close()

file = open(os.getcwd()+"/bacon.txt", 'a')
file.write("bacon is not vegetable!\n")
file.close()
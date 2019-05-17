import os

# get current path
os.getcwd()
# change current path
os.chdir('C:\\Windows\\System32')
# create directory
os.makedirs('C:\\delicious\\walnut\\waffles')


# get absolute directory
os.path.abspath('.\\Scripts') 'C:\\Python34\\Scripts'
# check if abs directory
os.path.isabs('.')
# get relative directory
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs') # '..\\..\\Windows'


path = 'C:\\Windows\\System32\\calc.exe'
# get last part
os.path.basename(path)	# 'calc.exe'
# get dir except last part
os.path.dirname(path)	# 'C:\\Windows\\System32'
# get two parts simultaneously
os.path.split(path)		# ('C:\\Windows\\System32', 'calc.exe')
# split all parts apart
path.split(os.path.sep) # ['C:', 'Windows', 'System32', 'calc.exe']


# get size of file
os.path.getsize(path)
# get filename list of directory
os.listdir(directory)


# check if file or directory path exists
os.path.exists(path)
# check if path is file
os.path.isfile(path)
# check if path is directory
os.path.isdir(path)


# open, read, write too simple
# just skip it


# save variabls

# method 1: shelve
import shelve
shelfFile = shelve.open('shelfFilePath')
mycats = ['Zophie', 'Pooka', 'Simon']
shelfFile['mycats'] = mycats
shelfFile.close()

# method 2: pprint.pformat()
import pprint
mycats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(mycats) # "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('mycats = ' + pprint.pformat(mycats) + '\n')
fileObj.close()
# import py file directly
import myCats
myCats.mycats



import os 
import shutil
source=input('Enter source folder name')
dest = input('Enter destination folder name')

source=source+"/"
dest=dest+"/"

list_of_files =os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),dest)
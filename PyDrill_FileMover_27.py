import shutil
import os


src = 'C:/Users/V/Desktop/Folder A/'
dst = 'C:/Users/V/Desktop/Folder B/'

srcfiles = os.listdir(src)

for file in srcfiles:
    if file.endswith (".txt"):
        shutil.move(src+file, dst)

print (dst)

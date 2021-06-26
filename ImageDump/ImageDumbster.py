import os
import shutil

directory = "ImageDumbster"
enteries = os.listdir('/Users/danielzeglen/Desktop')
parent_dir = '/Users/danielzeglen/Desktop'
path = os.path.join(parent_dir, directory)


if os.path.exists(path):
    
    print('file is there')
else:
    os.mkdir(path)
    print('no such file')

for file in enteries:
    if '.png' in file or '.jpeg' in file:
        source = os.path.join(parent_dir, file)
        shutil.move(source,path)
        print(file)




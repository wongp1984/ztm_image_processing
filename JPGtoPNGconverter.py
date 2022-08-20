import sys
import os 
from PIL import Image

src_dir = sys.argv[1]
dest_dir = sys.argv[2]

if (not os.path.exists(src_dir)):
    print(f'Source folder {src_dir} does not exit.  Program is terminated!') #quit if the source folder not exists
else:
    if (not os.path.exists(dest_dir)):
        print(f'Destination folder {dest_dir} is created.')  #create the destination folder if not exist
        os.mkdir(dest_dir) 

for (root,dirs,files) in os.walk(src_dir, topdown=True):  #iterate the subfolders 
        for file in files:
            src_file = os.path.join( root, file)  
            
            if os.path.splitext(src_file)[1].lower().endswith("jpg"):
                dest_file = os.path.join( root.replace(src_dir,dest_dir), file) 
               
                dest_file = os.path.splitext(dest_file)[0] + '.png'  #generate the destination file name 
                print(dest_file)
                with Image.open(src_file) as img:
                    img.save(dest_file, 'png')  # convert the source jpg file to png file in the destination folder


           


import os
import numpy as np
from PIL import Image
from pathlib import Path
import sys

def crop_image(base_name, mask_name, start_dir, end_dir):
    mask = Image.open(mask_name)
    base = Image.open(start_dir + '\\' + base_name)
    mask_arr = np.array(mask)
    base_arr = np.array(base)
    
    if(mask_arr.shape != base_arr.shape):
        print('error: file not right shape')
        return

    print(mask_arr[124, 124])
    print(mask.format, mask.size, mask.mode)
    print(mask_arr.shape)

    x, y = mask_arr.shape[0], mask_arr.shape[1]
    print(x, y)

    for a in range(x):
        for b in range(y):
            if(not (mask_arr[a][b][0] == 0 and mask_arr[a][b][1] == 0 and 
                    mask_arr[a][b][2] == 0 and mask_arr[a][b][3] == 255)):
                base_arr[a][b][0] = mask_arr[a][b][0]
                base_arr[a][b][1] = mask_arr[a][b][1]
                base_arr[a][b][2] = mask_arr[a][b][2]
                base_arr[a][b][3] = mask_arr[a][b][3]
    file_parts = base_name.split('.')
    print(file_parts)
    mod_img = Image.fromarray(base_arr)
    mod_img.save(end_dir + '\\' + file_parts[0] + '_token' + '.' + file_parts[1])
    print(" ")
    
if(len(sys.argv) < 2):
    print("enter a folder on the command line")
    exit()

folder = sys.argv[1]

curdir = os.getcwd()
print(curdir)

if(not os.path.isdir(curdir + '\\' + folder)):
    os.mkdir(folder)
if(not os.path.isdir(curdir + '\\' + folder + '_tokens')):
    os.mkdir(folder + '_tokens')


files = os.listdir(curdir + '\\' + folder)
print(files)

for file in files:
    if(file.endswith('.png')):
        crop_image(file, 'mask3.png', folder, folder + '_tokens')

print('all done')
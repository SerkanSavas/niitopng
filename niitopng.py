import os
import numpy as np
import nibabel as nib
import imageio

path1 = 'input'   #path of folder of images    
path2 = 'output'  #path of folder to save images    
listing = sorted(os.listdir(path1)) 
num_samples=np.size(listing)
count=0

for file in listing:
    img = nib.load(path1 +"\\" + file)
    imgData= img.get_fdata()
    (x,y,z) = imgData.shape
    slc1=round(z/2) #to get the mid frame
    slc2=slc1-1     #to get one before
    img1=imgData[:,:,slc1] #if you want specific frame, you can define number
    img2=imgData[:,:,slc2] #if you want specific frame, you can define number
    imageio.imwrite(os.path.join(path2,'{}slc1.png'.format(file)),img1)
    imageio.imwrite(os.path.join(path2,'{}slc2.png'.format(file)),img2)
    count +=1
print( count, " images converted and",count*2," images saved")
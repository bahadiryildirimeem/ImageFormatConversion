
# coding: utf-8

# In[51]:


import cv2
import os
import sys

# get output img format
outImgType = '.'+sys.argv[1]
imgName = sys.argv[2]
startingIndex = int(sys.argv[3])

in_path = 'input'
out_path = 'output'
#get dir's all file's filename
files= os.listdir(in_path)
for filename in files: 
    name = filename.split('.')
    if not os.path.isdir(filename):  
        inImg =os.path.join(in_path,filename)
        img = cv2.imread(inImg)
        outImg = os.path.join(out_path,imgName+str(startingIndex)+outImgType)
        startingIndex = startingIndex + 1
        print(inImg,outImg,cv2.imwrite(outImg,img))

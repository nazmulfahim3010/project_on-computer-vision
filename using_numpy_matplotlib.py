import  numpy as np #type:ignore
import matplotlib.pyplot as plt#type:ignore
import cv2 #type:ignore

image=cv2.imread('fam.jpg')
plt.imshow(image)
rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# plt.imshow(rgb_image)
plt.waitforbuttonpress()
plt.close("all")
##it use RGB but cv2 use BGR thats why color is different


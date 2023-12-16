import cv2
import numpy as np

path = input("Enter Path :-")
try:
    img = cv2.imread(path)
    cv2.imshow("img",img)

except Exception:
    print("Path not found")
    exit()

array = np.array(img)
unique,counts = np.unique(array,return_counts=True)
ocurrance = dct(zip(unique,counts))

a1_sorted_keys = sorted(ocurrance,key=ocurrance.get,reverse=True)
print(a1_sorted_keys[:3])
image = np.zeros((300,300,3),np.uint8)
image[:] = a1_sorted_keys[:3]
c=a1_sorted_keys[0]
color =np.zeros((300,300,3),np.uint8)
color[:] = (c,c,c)
print("Tone :" + str(a1_sorted_keys[:3]))
cv2.imshow("Tone",image)
print("color:"+str([c,c,c]))
cv2.imshow("color",color)

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


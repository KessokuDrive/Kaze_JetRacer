from test_upload import *
import time
import numpy as np

t_all = []

globalTime = time.time()
count = 0

test_image = cv2.imread("./EtTlIdw_1.png")
while True:
    check = time.time()
    if(int((check - globalTime)%60)>=10):
        break
    t1 = time.time()
    demo(test_image)
    count+=1
    t2 = time.time()
    t_all.append(t2 - t1)

print('average time:', np.mean(t_all) / 1)
print('average fps:',1 / np.mean(t_all))
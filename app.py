# load dependencies
import cv2
import os
import time
import uuid

# create folders and labels
image_path = '\images'

labels = ['Rolling Hand Backward', 'Rolling Hand Forward', 'Stop', 'Swiping Left', 'Swiping Right', 'No Gesture'  ]


dim = (300, 300)


numberof_images = 48

for label in labels:
    os.makedirs(f"{label}")
    cap = cv2.VideoCapture(0) # capture video from the device camera
    print(f'Collect Images for label: {label}')
    time.sleep(4)
    
    for imgnum in range(numberof_images):
        ret, frame = cap.read()
        imgname = os.path.join(label,label+f'.{imgnum}.jpg')
        print('Original Dimensions : ',frame.shape)
        frame = cv2.resize(frame,(300,300))
        print('\tresized Dimensions : ',frame.shape)
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame',frame)
        time.sleep(1)

    cap.release()
    cv2.destroyAllWindows()
 
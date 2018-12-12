#This script is to be run on the client side of the network, to capture video served from a raspberry pi using a tcp protocol.

#cv2 extracts a frame of video from the stream, using automatically identified codecs, then converts the rgb image to gray and displays the frame


import cv2


vc = cv2.VideoCapture('tcp://IP-ADDRESS_OF_PI:PORT')


while True:

    ret,frame = vc.read()
    print(type(frame))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edgemap = cv2.Canny(gray,100,200)[:,::-1]
    
    
    cv2.imshow('frame', edgemap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

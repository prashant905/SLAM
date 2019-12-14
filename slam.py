import cv2
from display import Display
import time
from Extractor import  Extractor
from skimage import data, io, filters
import numpy as np

W = 1920//2
H = 1080//2

screen = Display(W,H)
fe =Extractor()

def process_frame(img):
    img = cv2.resize(img,(W,H))
    matches = fe.extractfeature(img)
    print('{} matches'.format(len(matches)))
    if matches is None:
        return
    # for p in kps:
    #     u,v  = map(lambda x: int(round(x)),p.pt)
    #     cv2.circle(img, (u,v),color=(0,255,0),radius=3)
    for pt1,pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1.pt)
        u2, v2 = map(lambda x: int(round(x)), pt2.pt)

        cv2.circle(img, (u1,v1),color=(0,255,0),radius=3)
        cv2.line(img,(u1,v1),(u2,v2), color=(255,0,0))
    screen.paint(img)

if __name__ == '__main__':
    cap = cv2.VideoCapture('test2.mp4')
    while cap.isOpened():
        ret,frame = cap.read()
        if ret ==True:
            process_frame(frame)
        else:
            break

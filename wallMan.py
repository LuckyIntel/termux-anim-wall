from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, imwrite
from time import sleep
from os import system

def render(video: VideoCapture, targetFPS: int):
    frame = 0
    suc, img = video.read()
    
    while suc:
        imwrite("wallpaper\\frame.jpg", img)

        system("termux-wallpaper -f wallpaper\\frame.jpg")

        suc, img = video.read()

        if frame == video.get(CAP_PROP_FRAME_COUNT): frame = 0
        else: frame += 1

        print(frame)

        sleep(1 / targetFPS)
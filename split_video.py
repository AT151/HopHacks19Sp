import cv2
import os

def FrameCapture(in_path, out_path):
    vidObv = cv2.VideoCapture(in_path)
    count = 0
    success = 1
    while success:
        success, image = vidObv.read()
        out = out_path + "/frame" + str(count) + ".jpg"
        print(out)
        cv2.imwrite(out, image)
        count += 1
    print(in_path, out_path)
if __name__ == '__main__':
    for folder in os.listdir("./videos/"):
        for file in os.listdir("./videos/" + folder + "/"):
            FrameCapture("./videos/" + folder + "/" + file, "./pictures/" + folder)

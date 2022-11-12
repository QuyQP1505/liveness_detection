import os 
import cv2
import shutil

csv_path = r"D:\Github\Face-Liveness-Detection\data\lable_frames.csv"
img_folder = r"D:\Github\Face-Liveness-Detection\data\frames"
fake_img_folder = r"D:\Github\Face-Liveness-Detection\data\fake"
real_img_folder = r"D:\Github\Face-Liveness-Detection\data\real"

with open(csv_path, "r+") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        split_line = line.split(",")
        idx,filename,label = split_line
        if filename == 'Frame':
            pass
        else:
            cur_image = os.path.join(img_folder, filename)
            if label == str(0.0):
                shutil.move(
                    cur_image, os.path.join(fake_img_folder, filename)
                )
            else:
                shutil.move(
                    cur_image, os.path.join(real_img_folder, filename)
                )

print("Done!")
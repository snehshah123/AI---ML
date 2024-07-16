import cv2
from ultralytics import YOLO

model = YOLO('yolov8m.pt')
model.train(data=r"G:\SRAV2\New\Labelled Apple-Orange\data.yaml",epochs = 2)
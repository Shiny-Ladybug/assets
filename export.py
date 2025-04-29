from ultralytics import YOLO
import os
import onnxruntime

model = YOLO("./afk-seg.pt")

model.export(format='onnx', dynamic=True)

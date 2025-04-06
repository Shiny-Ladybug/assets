from ultralytics import YOLO
import os

models = [os.path.join("./", model)
          for model in os.listdir("./") if model.endswith(".pt")]
print(models)
for model in models:
    if os.path.exists(model):
        yolo_model = YOLO(model)
        names = yolo_model.names
        print(f"* model: {model}  ")
        yolo_model.info()
        print(f"  classes: {yolo_model.model.names}  ")

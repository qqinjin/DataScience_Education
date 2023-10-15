from ultralytics import YOLO

model = YOLO(r'C:\Users\jae12\Desktop\pycode\화재검출서비스\yolov8\best8.pt')
results = model(r'C:\Users\jae12\Desktop\pycode\화재검출서비스\yolov8\hf.mp4', save=True)
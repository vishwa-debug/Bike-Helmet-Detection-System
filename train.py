from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="Helmet-No-Helmet.v1i.yolov8/data.yaml",
    epochs=10,
    imgsz=416,
    batch=8,
    project="runs",
    name="helmet_detection"
)
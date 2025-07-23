import os
import cv2
import torch
import requests
import numpy as np
from flask import Flask, render_template, request
from PIL import Image
from deepface import DeepFace
from torchvision import models, transforms

app = Flask(__name__)

# Load YOLOv8 model
from ultralytics import YOLO
yolo_model = YOLO("yolov8m.pt")

# Load ImageNet class labels
imagenet_file = "imagenet_classes.txt"
try:
    with open(imagenet_file, "r") as f:
        imagenet_labels = dict(enumerate([line.strip() for line in f.readlines()]))
except FileNotFoundError:
    url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    response = requests.get(url)
    with open(imagenet_file, "w") as f:
        f.write(response.text)
    imagenet_labels = dict(enumerate(response.text.strip().split("\n")))

# Load ResNet for classification
resnet = models.resnet50(pretrained=True)
resnet.eval()

# Image preprocessor
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        file = request.files["image"]
        image_path = os.path.join("static", file.filename)
        file.save(image_path)

        img = cv2.imread(image_path)

        # Use YOLO to detect
        detections = yolo_model(img)[0]

        for box in detections.boxes:
            cls_id = int(box.cls[0])
            label = yolo_model.names[cls_id]

            if label.lower() == "person":
                try:
                    analysis = DeepFace.analyze(img_path=image_path, actions=["age", "gender"], enforce_detection=True)
                    age = analysis[0]["age"]
                    gender = max(analysis[0]["gender"], key=analysis[0]["gender"].get)

                    result = f"Species: Human | Age: {age} | Gender: {gender}"
                except Exception as e:
                    result = f"Human detected but age/gender couldn't be analyzed: {str(e)}"
            else:
                # If animal or bird
                image = Image.open(image_path).convert("RGB")
                input_tensor = transform(image).unsqueeze(0)
                with torch.no_grad():
                    outputs = resnet(input_tensor)
                _, predicted = outputs.max(1)
                species = imagenet_labels[int(predicted.item())]
                result = f"Species: {species}"

        return render_template("index.html", result=result, image=image_path)

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

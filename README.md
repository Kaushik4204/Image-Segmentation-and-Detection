Image Classification & Human Attribute Detection Web App

This is a Flask-based web application that allows users to upload an image and identify:

- 🐶 Animal or bird species using **YOLOv8 + ResNet50**
- 👤 If it's a human, detect **Age** and **Gender** using **DeepFace**

---

## 🚀 Features

- ✅ Object detection with **YOLOv8**
- ✅ Human face analysis with **DeepFace**
- ✅ Animal/bird species classification using **ResNet50**
- ✅ Fully responsive frontend (styled with HTML/CSS)
- ✅ Runs locally on your machine

---

## 📸 Sample Output

## **Input**

<img width="1357" height="601" alt="image" src="https://github.com/user-attachments/assets/dec90331-d374-490b-beb6-980e166c4351" />

---

## **output**

<img width="1365" height="767" alt="Screenshot 2025-07-21 222943" src="https://github.com/user-attachments/assets/5480d28b-c4f0-40bc-ad50-bcb5cca0a436" />
<img width="1365" height="767" alt="Screenshot 2025-07-21 223149" src="https://github.com/user-attachments/assets/20c05a35-3cf8-4cf1-9722-ee86f0fcd4da" />
<img width="1365" height="767" alt="Screenshot 2025-07-21 222913" src="https://github.com/user-attachments/assets/2f21f4de-3b52-49e4-b730-208ea73cc32e" />



---

## 🧰 Tech Stack

| Layer        | Technology Used            |
|--------------|----------------------------|
| Backend      | Python, Flask              |
| Deep Learning| YOLOv8, DeepFace, ResNet50 |
| Frontend     | HTML, CSS                  |
| Deployment   | Localhost (Flask)          |

---

## 📁 Project Structure

├── static/

│ └── uploaded images

├── templates/

│ └── index.html

├── app.py

├── yolov8m.pt

├── imagenet_classes.txt

├── requirements.txt

└── README.md



---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/image-analyzer-app.git
   cd image-analyzer-app
Create and activate a virtual environment (optional but recommended):


   ```bash
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies:
   ```

   ```bash

pip install -r requirements.txt
Run the Flask app:
   ```


   ```bash
python app.py

   ```
🖼️ UI Overview
mathematica
Copy
Edit
[ Upload Image Button ]
[ Analyze Button ]
[ Result Box → Species / Age / Gender ]
[ Image Preview Box ]
📌 Notes
Ensure yolov8m.pt is present in your project directory.

If imagenet_classes.txt is missing, it will be downloaded automatically.

Gender output is cleaned to display only "Male" or "Female" instead of confidence scores.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


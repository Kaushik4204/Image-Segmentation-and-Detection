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

- **Input**: Image of a person  
- **Output**:  
  - Species: Human  
  - Age: 28  
  - Gender: Male  
  - [Image preview shown on result page]

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

yaml
Copy
Edit

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/image-analyzer-app.git
   cd image-analyzer-app
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
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


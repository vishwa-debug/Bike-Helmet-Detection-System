# 🏍️ Bike Helmet Detection System

An AI-powered computer vision project that detects whether a motorcycle rider is wearing a helmet using **YOLOv8, Python, and Streamlit**. The system analyzes images and displays detection results to demonstrate how deep learning can support road safety monitoring.

## 📌 Project Overview

Wearing a helmet is essential for motorcycle rider safety. This project explores the use of object detection to identify helmets in images and visualize the model's predictions.

The system uses a trained YOLOv8 object detection model to identify helmet-related objects and display bounding boxes around detected objects.

## ✨ Features

- 🪖 **Helmet Detection:** Detects helmets in input images.
- 🚫 **No-Helmet Detection:** Supports no-helmet detection when the trained model includes this class.
- 🎯 **Object Localization:** Displays bounding boxes and class labels.
- 📊 **Confidence Scores:** Shows model confidence for predictions when enabled.
- 🖥️ **Interactive Web Interface:** Uses Streamlit for a simple user interface.
- 📷 **Visual Results:** Displays the processed image with detection results.

## 🧰 Technologies Used

- **Programming Language:** Python
- **Object Detection:** YOLOv8
- **Computer Vision:** OpenCV
- **Deep Learning Framework:** PyTorch
- **Web Interface:** Streamlit
- **Image Processing:** NumPy
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
helmet-detection/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Files excluded from Git
│
├── models/
│   └── best.pt             # Trained model weights (if included)
│
├── sample_images/          # Optional test images
│
└── outputs/                # Optional detection results
```

*Note: Adjust this structure to match your actual repository. Do not upload model weights or image folders unless they are present and appropriate to share.*

## ⚙️ Installation

### 1. Clone the repository

Replace the URL below with your actual public GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd helmet-detection
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, the basic packages may include:

```bash
pip install ultralytics streamlit opencv-python numpy pillow
```

## ▶️ Run the Application

Start the Streamlit application from the project directory:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

Upload an image through the interface to view the detection results.

**Important:** Ensure that `app.py` references the correct trained model path and that the required model weights are available before running the application.

## 🔍 How It Works

1. **Image Input:** The user uploads an image through the Streamlit interface.
2. **Preprocessing:** The image is prepared for model inference.
3. **YOLOv8 Inference:** The trained model predicts objects in the image.
4. **Detection Results:** The model returns class labels, bounding boxes, and confidence scores.
5. **Visualization:** The application displays the annotated image.

## 🖼️ Sample Output

Add your actual output image to the repository and update the filename below.

![Bike Helmet Detection Result](docs/images/helmet-detection-result.png)

*Example: Annotated motorcycle image showing the objects detected by the model.*

## 📈 Model Performance

The model was trained for 10 epochs. The recorded evaluation metrics from the current experiment are:

| Metric | Recorded Value |
|---|---:|
| Precision | 0.948 |
| Recall | 0.895 |
| mAP@50 | 0.958 |
| mAP@50–95 | 0.774 |

These are the recorded metrics from the current training experiment. Performance may vary on new images and real-world conditions.

## 🚀 Future Improvements

- Improve detection across different lighting and weather conditions.
- Test the model on diverse motorcycle images.
- Extend the application to support video input.
- Explore real-time detection using a camera.
- Evaluate performance on unseen test data.
- Explore integration with traffic monitoring systems.

## 🎯 Applications

- Motorcycle road safety research
- Helmet compliance monitoring prototypes
- Intelligent transportation systems
- Computer vision and object detection learning
- AI-powered traffic monitoring experiments

## 👨‍💻 Author

**Vishwa N**

AI & Machine Learning | Computer Vision | Deep Learning

- GitHub: [vishwa-debug](https://github.com/vishwa-debug)
- Project: [Bike Helmet Detection System](YOUR_GITHUB_REPOSITORY_URL)

## ⚠️ Disclaimer

This project is an educational computer vision prototype. It is not a certified road-safety enforcement system. Predictions may be incorrect, and real-world deployment requires additional validation.

## 📄 License

Add an open-source license, such as the MIT License, if you want to permit reuse under its terms.

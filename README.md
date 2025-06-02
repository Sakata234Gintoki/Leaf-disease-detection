# 🌿 Leaf Disease Detection using InceptionV3

This project uses the **InceptionV3** deep learning model to detect diseases in plant leaves with high accuracy. The tool helps in early identification of plant diseases to support farmers and researchers in improving crop health and yield.

## 🚀 Live Demo

Try the live web app on Hugging Face Spaces:

👉 [Click here to try it out](https://huggingface.co/spaces/Noy10/Leaf_disease_detection)

## 🧠 Model Overview

- **Model Used**: InceptionV3
- **Training Accuracy**: 95.80%
- **Validation Accuracy**: 96.01%
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam

The model was fine-tuned on a custom dataset of leaf images and demonstrates strong generalization for multiple disease classes.

## 📊 Dataset

- **Classes**: Healthy, Powdery Mildew, Rust, Leaf Spot, etc.
- **Preprocessing**: Image resizing, normalization
- **Augmentation**: Rotation, flipping, zoom, brightness

## 🛠️ Technologies

- Python
- TensorFlow / Keras
- OpenCV
- Gradio
- Hugging Face Spaces

## 🖥️ Features of the Web App

- Upload a leaf image.
- Get instant prediction of the disease.
- View model confidence scores.

## 📁 Project Structure
<pre> inception-leaf-disease/ 
  ├── inception_model.h5 # Trained InceptionV3 model
  ├── app.py # Gradio app code
  ├── requirements.txt # Python dependencies
  ├── README.md # Project overview
   </pre>
## 📈 Results

The **InceptionV3** model achieved excellent performance on the validation set, demonstrating strong generalization across multiple leaf disease classes.

| Metric       | Value      |
|--------------|------------|
| Accuracy     | 96.01%     |
| Precision    | 95.8%      |
| Recall       | 96.2%      |
| F1-Score     | 96.0%      |
| Validation Loss | 0.11   |

- The model shows high precision and recall, indicating it's both accurate and consistent.
- Disease class predictions are well-separated, with minimal confusion.
- Training and validation loss curves show no overfitting.


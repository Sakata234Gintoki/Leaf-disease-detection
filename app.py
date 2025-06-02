import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = load_model("best_model.keras")

# Class labels mapping
class_labels = {
    0: 'Pepper bell Bacterial_spot',
    1: 'Pepper bell healthy',
    2: 'Potato Early blight',
    3: 'Potato Late blight',
    4: 'Potato healthy',
    5: 'Tomato Bacterial spot',
    6: 'Tomato Early blight',
    7: 'Tomato Late blight',
    8: 'Tomato Leaf Mold',
    9: 'Tomato Septoria leaf spot',
    10: 'Tomato Spider mites Two spotted spider mite',
    11: 'Tomato Target Spot',
    12: 'Tomato Tomato YellowLeaf Curl_Virus',
    13: 'Tomato Tomato mosaic virus',
    14: 'Tomato healthy'
}

# Function to process the image and make predictions
def predict(img):
    img = img.resize((224, 224))  # Resize the image
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_label = class_labels[predicted_class_index]  # Map index to class label

    return f"🌿 Predicted Class: {predicted_label}"

# Custom CSS for animations
custom_css = """
.gradio-container {
    background: url('https://images.unsplash.com/photo-1560807707-8cc77767d783') no-repeat center center fixed;
    background-size: cover;
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

h1, h3 {
    text-align: center;
    color: white;
    font-family: 'Arial', sans-serif;
}

#image-upload {
    animation: scaleUp 1s ease-in-out;
}

@keyframes scaleUp {
    from { transform: scale(0.9); }
    to { transform: scale(1); }
}

button {
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    background-color: #45a049;
    transform: scale(1.1);
}
"""

# Gradio Interface with animated UI
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<h1>🌱 Leaf Disease Classifier 🚜</h1>")
    gr.Markdown("<h3>Upload an image of a leaf to detect diseases</h3>")
    
    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload Leaf Image", elem_id="image-upload")
        output_text = gr.Textbox(label="Prediction", interactive=False)

    btn = gr.Button("Analyze Leaf 🌿")
    btn.click(fn=predict, inputs=image_input, outputs=output_text)

demo.launch()





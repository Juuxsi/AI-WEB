import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os
from tensorflow.keras.applications.efficientnet import preprocess_input

# -----------------------------
# PATH
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class_names_path = os.path.join(BASE_DIR, "class_names (1).json")
model_path = os.path.join(BASE_DIR, "dog_breed_model1.keras")

# -----------------------------
# LOAD CLASS NAMES
# -----------------------------
with open(class_names_path, "r", encoding="utf-8") as f:
    class_names = json.load(f)

# -----------------------------
# LOAD MODEL
# -----------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(
        model_path,
        custom_objects={"preprocess_input": preprocess_input}
    )
    return model

# -----------------------------
# IMAGE PREPROCESS
# -----------------------------
def preprocess_image(image):

    img = image.resize((224, 224))
    img = np.array(img)

    img = preprocess_input(img)

    img = np.expand_dims(img, axis=0)

    return img

# -----------------------------
# APP
# -----------------------------
def app():

    st.title("🐶 Dog Breed Predictor")
    st.write("Upload a dog image to predict its breed")

    uploaded_file = st.file_uploader(
        "Upload Dog Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        try:

            model = load_model()

            image = Image.open(uploaded_file).convert("RGB")

            st.image(image, caption="Uploaded Image", use_column_width=True)

            img = preprocess_image(image)

            prediction = model.predict(img)

            prediction = prediction[0]

            if len(prediction) != len(class_names):

                st.error(
                    f"Model output ({len(prediction)}) "
                    f"ไม่ตรงกับ class_names ({len(class_names)})"
                )
                return

            predicted_class = np.argmax(prediction)

            st.success(
                f"Prediction: **{class_names[predicted_class]}**"
            )

            st.subheader("Top 5 Predictions")

            top5 = np.argsort(prediction)[-5:][::-1]

            for i in top5:

                breed = class_names[i]
                prob = prediction[i] * 100

                st.write(f"{breed} : {prob:.2f}%")

        except Exception as e:

            st.error(f"Prediction Error: {e}")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    app()
import streamlit as st
import requests
from PIL import Image
import io

# Define the FastAPI server URL
FASTAPI_URL = "http://localhost:800/predict"  # Update with your FastAPI server URL

# Streamlit App Title
st.title("Image Classification with FastAPI and Streamlit")

# File Upload Section
st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Prediction Button
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            # Send the image to the FastAPI server for prediction
            response = requests.post(FASTAPI_URL, files={"file": uploaded_file})
            
            if response.status_code == 200:
                prediction = response.json()
                st.success(f"Prediction: {prediction['class']} (Confidence: {prediction['confidence']:.2f})")
            else:
                st.error("Prediction failed. Please try again.")

# Additional Information
st.sidebar.header("About")
st.sidebar.info(
    "This is a Streamlit web application that uses a FastAPI server for image classification. Upload an image, and it will be sent to the FastAPI server for prediction."
)

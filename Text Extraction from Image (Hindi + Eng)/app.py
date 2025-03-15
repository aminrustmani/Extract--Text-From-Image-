import streamlit as st
import google.generativeai as genai
import os
import PIL.Image

# Set API Key for Google Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyBrCkMY7zAvn4t2Ptq-RsMV9RLzbJJI6ps"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load the Gemini Model
model = genai.GenerativeModel("models/gemini-2.0-flash-001")


# Function to extract text from an image using Gemini
def extract_text_from_image(image):
    prompt = """
    You are an expert in Optical Character Recognition (OCR). 
    Extract and return all readable text from the given image. 
    Maintain proper formatting and spacing.
    If no text is detected, return "No readable text found."
    """

    response = model.generate_content([prompt, image])
    return response.text.strip()


# Streamlit UI
st.title("Image Text Extractor using Google Gemini")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        extracted_text = extract_text_from_image(image)
        st.subheader("Extracted Text:")
        st.write(extracted_text)

import streamlit as st
import requests

# When running locally, FastAPI runs on 8000
# When deployed, replace with your actual FastAPI URL
FASTAPI_URL = "https://dl-car-damage-detection.onrender.com/predict"

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the Car Image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analysing damage..."):
        try:
            # Send image bytes directly to FastAPI — no need to save to disk
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "image/jpeg")}
            response = requests.post(FASTAPI_URL, files=files,timeout=120)

            if response.status_code == 200:
                result = response.json()
                if "prediction" in result:
                    st.success(f"Detected Damage: {result['prediction']}")
                else:
                    st.error(f"Server error: {result.get('error', 'Unknown error')}")
            else:
                st.error(f"Request failed with status code {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the prediction server. Is FastAPI running?")
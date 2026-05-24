import streamlit as st
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file=st.file_uploader("Upload the Car Image",type=["jpg","png"])

if uploaded_file:
    image_path="temp_file.jpg"
    with open(image_path,"wb") as f: # wb means write binary, f is the file handler
        f.write(uploaded_file.getbuffer()) # uploaded image is converted to binary data and that binary data is written to a file
        st.image(uploaded_file,caption="Uploaded File",use_container_width=True)
        prediction=predict(image_path)
        st.success(f"Detected Damage: {prediction}")
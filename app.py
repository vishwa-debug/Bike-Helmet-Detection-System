import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Helmet Detection",
    page_icon="⛑️"
)

st.title("⛑️ Worksite Helmet Detection")
st.write("AI-based detection of Helmet and No-Helmet cases.")

model = YOLO("runs/detect/runs/helmet_detection/weights/best.pt")

uploaded_file = st.file_uploader(
    "Upload a worksite image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Input Image")
    st.image(image, width="stretch")

    with tempfile.NamedTemporaryFile(
        suffix=".jpg",
        delete=False
    ) as temp:
        image.save(temp.name)

        results = model.predict(
            source=temp.name,
            conf=0.25
        )

    result_image = results[0].plot()

    st.subheader("Detection Result")
    st.image(
    result_image,
    channels="BGR",
    width="stretch"
    )

    st.success("Detection completed successfully.")
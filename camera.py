import streamlit as st
from PIL import Image
import io
from datetime import datetime


st.set_page_config(page_title="📷 Ultimate Camera App")
st.title(" Ultimate Camera App — Capture, Save & Download")
st.caption("Take a photo using your webcam, preview it, save it to your system, and download it instantly.")

st.markdown("---")


col1, col2 = st.columns(2)


with col1:
    st.header(" Step 1: Capture Image")
    img_file = st.camera_input("Take a picture from your webcam:")


with col2:
    st.header("Step 2: Preview Your Capture")

    if img_file:
        image = Image.open(img_file)
        st.image(image, caption="Your Captured Image", use_container_width=True)

        
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        
        file_name = f"captured_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        
        st.download_button(
            label=" Download Captured Image",
            data=img_bytes,
            file_name=file_name,
            mime="image/png"
        )
    else:
        st.info(" Please capture an image to preview it here.")


  
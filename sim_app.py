import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("Sim App")
st.write("Hello Dennis! This is your first app.")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome, {name}!")

st.divider()
st.subheader("📷 Scan Serial Barcode")
st.write("Tap 'Take Photo' and point your camera at the barcode.")

photo = st.camera_input("Take a photo of the barcode")

if photo:
    image = Image.open(photo)
    img_array = np.array(image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Try QR code first
    qr_detector = cv2.QRCodeDetector()
    qr_data, _, _ = qr_detector.detectAndDecode(img_cv)

    # Try barcode
    barcode_data = ""
    try:
        barcode_detector = cv2.barcode_BarcodeDetector()
        retval, decoded_info, _, _ = barcode_detector.detectAndDecodeWithType(img_cv)
        if retval and decoded_info:
            barcode_data = decoded_info[0]
    except Exception:
        pass

    result = qr_data or barcode_data

    if result:
        st.success(f"✅ Scanned Code: {result}")
        st.code(result)
    else:
        st.warning("Could not read barcode. Try again - hold steady, good light, fill the frame with the barcode.")
        st.image(image, caption="Your photo")

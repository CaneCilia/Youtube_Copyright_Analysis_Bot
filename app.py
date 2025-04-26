import streamlit as st
from image_module import check_image
from video_module import check_video
from audio_module import check_audio

st.title("🛡️ Copyright Infringement Detector")

media_type = st.selectbox("Select Media Type", ["Image", "Video", "Audio"])

uploaded_file = st.file_uploader("Upload Media File", type=["jpg", "png", "mp4", "mp3", "wav"])

if uploaded_file:
    if media_type == "Image":
        result = check_image(uploaded_file)
    elif media_type == "Video":
        result = check_video(uploaded_file)
    elif media_type == "Audio":
        result = check_audio(uploaded_file)
        
    st.success(f"🧠 Result: {result['status']}")
    st.json(result)


import streamlit as st
import tempfile
import os
import cv2
from tracking import process_video

st.title("Motion Tracking in Drone Videos using FAST and ORB")

uploaded_file = st.file_uploader("Upload a drone video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    stframe = st.empty()  # Placeholder for video display

    def show_frame(frame):
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_container_width=True)

    with st.spinner("Processing video..."):
        success, result = process_video(video_path, output_path="output.mp4", display_callback=show_frame)

    if success:
        st.success("Video processed successfully.")
        with open(result, "rb") as f:
            st.download_button("Download Processed Video", f, file_name="tracked_output.mp4")
    else:
        st.error(result)

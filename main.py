import cv2
import gdown
import pandas as pd
from pathlib import Path
from moviepy.editor import VideoFileClip
import streamlit as st
from PIL import Image, ImageDraw, ImageFont


cwd = Path(".")
st.title("Video Transcription")

file_finder = cwd.glob("*.mov")
list_of_vids = [str(i) for i in file_finder]

if "Success4.mov" not in list_of_vids:
    url = "https://drive.google.com/uc?id=1kUO0dKTsq4E2rFH1_JehUZC23giwVtY3"
    output = "Success4.mov"
    gdown.download(url, output, quiet=False)


frame_index = -1
def pipeline(frame):
    global frame_index
    frame_index += 1
    try:
        global x
        cv2.putText(frame, str(frame_index), (0, 0), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
        x = frame
    except StopIteration:
        pass
    # additional frame manipulation
    return frame


# dfi = pd.DataFrame({'c1': [str(i) for i in range(160)]}).iterrows()

video = VideoFileClip("Success4.mov")
out_video = video.fl_image(pipeline)
out_video.write_videofile("color2.mp4", codec="libx264")

st.image(x)

st.video("color2.mp4")

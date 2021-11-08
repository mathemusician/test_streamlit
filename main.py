import cv2
import pandas as pd
from moviepy.editor import VideoFileClip
import streamlit as st


i = 0
def pipeline(frame):
    global i
    i += 1
    try:
        cv2.putText(frame, str(next(dfi)[1].item()), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA, True)
    except StopIteration:
        pass
    # additional frame manipulation
    return frame


dfi = pd.DataFrame({'c1': ["Hello", "World"]}).iterrows()

video = VideoFileClip("color.mp4")
out_video = video.fl_image(pipeline)
out_video.write_videofile("color2.mp4", codec="libx264")

st.write(i)

st.video("color2.mp4")

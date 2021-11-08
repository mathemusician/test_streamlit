import os
import streamlit as st
from moviepy.editor import ColorClip

st.write("Video Creation")

result = ColorClip(size=(200, 100), 
		   color=(0,0,0), 
		   duration=5).write_videofile('color.mp4', fps=24)


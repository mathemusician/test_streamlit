import streamlit as st
import gdown
from moviepy.editor import ColorClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

st.write("Video Creation")

if "Success4.mov" not in list_of_vids:
        url = "https://drive.google.com/uc?id=1kUO0dKTsq4E2rFH1_JehUZC23giwVtY3"
        output = "Success4.mov"
        gdown.download(url, output, quiet=False)
    
generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
subs = [((0, 4), 'subs1'),
        ((4, 9), 'subs2'),
        ((9, 12), 'subs3'),
        ((12, 16), 'subs4')]

subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("input.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


st.video('output.mp4')

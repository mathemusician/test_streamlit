import cv2
import pandas as pd
from moviepy.editor import VideoFileClip

def pipeline(frame):
    try:
        cv2.putText(frame, str(next(dfi)[1].sentence), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA, True)
    except StopIteration:
        pass
    # additional frame manipulation
    return frame


dfi = pd.DataFrame({'c1': ["Hello", "World"]}).iterrows()

video = VideoFileClip("output.mp4")
out_video = video.fl_image(pipeline)
out_video.write_videofile("color.mp4", audio=True)

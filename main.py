import streamlit as st
from pathlib import Path


file_path = Path("/etc/ImageMagick-6/policy.xml")

with open(file_path) as file_handler:
	lines = file_handler.readlines()

distasteful = [
	"  <!-- disable ghostscript format types -->\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"PS\" />\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"PS2\" />\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"PS3\" />\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"EPS\" />\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"PDF\" />\n",
	"  <policy domain=\"coder\" rights=\"none\" pattern=\"XPS\" />\n"
]
	
newlines = []
for line in lines:
	if line in distasteful:
		continue
	else:
		newlines.append(line)

newtext = "".join(newlines)

with open(file_path, "w") as file_handler:
	file_handler.write(newtext)

"""
# importing Numpy
import numpy as np

# importing moviepy module
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

# screen size
screensize = (720, 460)

# creating a text clip of color green, font is Arial and size is 80
txtClip = TextClip('GeeksforGeeks', color = 'lightgreen', font = "Arial",
				kerning = 5, fontsize = 80)

# creating a composite video of given size
cvc = CompositeVideoClip( [txtClip.set_pos('center')],
						size = screensize)

# helper function
rotMatrix = lambda a: np.array( [[np.cos(a), np.sin(a)],
								[-np.sin(a), np.cos(a)]] )


# creating a effect 1 method
def effect1(screenpos, i, nletters):
	
	# damping
	d = lambda t : 1.0/(0.3 + t**8)
	# angle of the movement
	a = i * np.pi / nletters
	
	# using helper function
	v = rotMatrix(a).dot([-1, 0])
	
	if i % 2 : v[1] = -v[1]
		
	# returning the function
	return lambda t: screenpos + 400 * d(t)*rotMatrix(0.5 * d(t)*a).dot(v)

# method for effect 2
def effect2(screenpos, i, nletters):
	
	# numpy array
	v = np.array([0, -1])
	
	d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1 + t**4))
	
	# returning the function
	return lambda t: screenpos + v * 400 * d(t-0.15 * i)



# a list of ImageClips
letters = findObjects(cvc)


# method to move letters
def moveLetters(letters, funcpos):
	
	return [ letter.set_pos(funcpos(letter.screenpos, i, len(letters)))
			for i, letter in enumerate(letters)]

# adding clips with specific effect
clips = [ CompositeVideoClip( moveLetters(letters, funcpos),
							size = screensize).subclip(0, 5)
		for funcpos in [effect1, effect2] ]

# comping all the clips
final_clip = concatenate_videoclips(clips)

# setting fps of the final clip
final_clip.fps = 24

# showing video clip
final_clip.ipython_display()
"""

  
  


"""
import torch
import librosa
import difflib
import soundfile
import numpy as np
import pickle as pl
from transformers import Wav2Vec2Processor
from pathlib import Path
from copy import deepcopy
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from flash.audio import SpeechRecognition, SpeechRecognitionData
import io
import scipy.signal as sps
from scipy.io import wavfile
"""

"""
uploaded_file = st.file_uploader("Choose an audio file")

if uploaded_file is not None:
  new_rate = 16000
  clip, sample_rate = soundfile.read(io.BytesIO(uploaded_file.read()))
  number_of_samples = round(len(clip) * float(new_rate) / sample_rate)
  clip = sps.resample(clip, number_of_samples)
  # b = bytes(str(b), "utf-8")
  # resampled_audio = librosa.resample(x, sr, 16000)
  # st.write(sr, x)
  # file_bytes = np.asarray(bytearray(uploaded_file.read()))
"""

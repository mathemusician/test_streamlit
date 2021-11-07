import streamlit as st
import gdown
import os
from pathlib import Path

cwd = Path(".")
st.title("Audio Transcription")

file_finder = cwd.glob("*.mov")
list_of_vids = [str(i) for i in file_finder]
st.write(list_of_vids)

if "Success4.mov" not in list_of_vids:
  url = "https://drive.google.com/uc?id=1kUO0dKTsq4E2rFH1_JehUZC23giwVtY3"
  output = "Success4.mov"
  gdown.download(url, output, quiet=False)
  st.write("Got it second time")
else:
  st.write("Got it first time")

  
  


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

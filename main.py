import torch
import librosa
import difflib
import soundfile
import numpy as np
import pickle as pl
import streamlit as st
from transformers import Wav2Vec2Processor
from pathlib import Path
from copy import deepcopy
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from flash.audio import SpeechRecognition, SpeechRecognitionData
import io

st.title("Audio Transcription")


uploaded_file = st.file_uploader("Choose an audio file")

if uploaded_file is not None:
  sr, x = soundfile.read(io.BytesIO(uploaded_file.read()))
  # b = bytes(str(b), "utf-8")
  resampled_audio = librosa.resample(x, sr, 16000)
  # st.write(sr, x)
  # file_bytes = np.asarray(bytearray(uploaded_file.read()))

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
from consolidate import time_decoder
from split_texts import split_by_words
from make_xml import make_xml_from_words
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from flash.audio import SpeechRecognition, SpeechRecognitionData

st.title("Audio Transcription")

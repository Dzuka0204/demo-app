import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_bytes = audio_recorder(energy_threshold=(-1.0, 1.0), pause_threshold=2.0,)
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
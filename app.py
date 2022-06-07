import streamlit as st
import os
import requests

st.set_page_config(
    page_title="Speech-to-Text Transcription App", page_icon="👄", layout="wide"
)

def _max_width_():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

_max_width_()



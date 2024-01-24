import streamlit as st
from manim_name import NameMerger
from manim import config
config.video_dir = "./"
config.output_file = "piui"
config.format = "mp4"
config.quality = "low_quality"

st.markdown("<h1 style='text-align: center; color: white;'>이름 궁합 계산기</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555555;'>commit.im@gmail.com</h3>", unsafe_allow_html=True)
input_string1 = st.text_input("이름 1")
input_string2 = st.text_input("이름 2")
if st.button("Match name"):
    if not (input_string1 and input_string2):
        st.warning("한글 이름을 입력해주세요", icon="⚠️")
    else:
        name_merger = NameMerger(input_string1, input_string2)
        name_merger.render()
        video_bytes = open("piui.mp4", "rb").read()
        st.video(video_bytes)
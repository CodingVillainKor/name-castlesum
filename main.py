import streamlit as st
from os import system

st.markdown("<h1 style='text-align: center; color: white;'>이름 궁합 계산기</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555555;'>commit.im@gmail.com</h3>", unsafe_allow_html=True)
input_string1 = st.text_input("이름 1")
input_string2 = st.text_input("이름 2")

temp_file_content = f"""
from manim_name import NameMerger
from manim import config

config.video_dir = "./"
config.output_file = "{input_string1}_{input_string2}"
config.format = "mp4"
config.quality = "low_quality"

name_merger = NameMerger("{input_string1}", "{input_string2}")
name_merger.render()
"""
def check_hangul(name):
    if not name: return False
    for c in name:
        if ord("가") <= ord(c) <= ord("힣"):
            continue
        else:
            return False
    return True

if st.button("Match name"):
    if not (check_hangul(input_string1) and check_hangul(input_string2)):
        st.warning("한글 이름을 입력해주세요", icon="⚠️")
    else:
        with open(f"{input_string1}_{input_string2}.py", "w", encoding="utf-8") as fw:
            fw.write(temp_file_content)
        system(f"python {input_string1}_{input_string2}.py")
        video_bytes = open(f"{input_string1}_{input_string2}.mp4", "rb").read()
        st.video(video_bytes)
        system(f"rm {input_string1}_{input_string2}.mp4")
        system(f"rm {input_string1}_{input_string2}.py")
import streamlit as st

with st.sidebar:
        st.header("프로필")
        user_name = st.text_input("닉네임")
        weather = st.selectbox("오늘날씨", ["맑음", "흐림", "비/눈", "매우 추움"])

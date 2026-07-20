import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
st.radio("학년", ["1", "2", "3"], horizontal=True)
st.number_input("반", min_value=1, max_value=11, value= 반)
난이도= st.select_slider("난이도",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
점수= st.slider("점수", 0, 100, 50)


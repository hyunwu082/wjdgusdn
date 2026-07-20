import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
st.radio("학년", ["1", "2", "3"], horizontal=True)
st.number_input("반", min_value=1, max_value=11, value= 반)
st.select_slider("응답 처리 속도를 선택하세요",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")

import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
st.radio("학년", ["1", "2", "3"], horizontal=True)
st.number_input("반", min_value=1, max_value=11, value=`반`)

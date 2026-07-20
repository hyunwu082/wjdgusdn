import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
grade= st.radio("학년", ["1", "2", "3"], horizontal=True)
반= st.number_input("반", min_value=1, max_value=11)
난이도= st.select_slider("난이도",options=["쉬움", "보통", "어려움"],value="보통")
점수= st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감입니다.")
if st.button("확인"):
        st.success(f")
        st.markdown(f"{user_id} /{grade}학년 / {반}반 / {난이도}")
        st.info(f"소감: {text}")
        
       

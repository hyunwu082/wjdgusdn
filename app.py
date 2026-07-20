import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
학년= st.radio("학년", ["1", "2", "3"], horizontal=True)
반= st.number_input("반", min_value=1, max_value=11, value= '반')
난이도= st.select_slider("난이도",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
점수= st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감입니다.")
if st.button("확인"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **이름:** {user_id}
        * **학년:** `{학년}` | **반:** `{반}`
        * **난이도:** {', '.join(난이도) if 난이도 else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
       

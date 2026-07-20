import streamlit as st

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0
    
if "typing_box" in st.session_state and st.session_state.typing_box != "":
    st.session_state.count += len(st.session_state.typing_box)
    st.session_state.typing_box = ""
    st.rerun()


st.text_input(
    "여기에 아무 키나 누르기",
    key="typing_box",
    label_visibility="collapsed",
)

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

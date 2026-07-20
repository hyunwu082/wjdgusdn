import streamlit as st
from streamlit_keyboard_shortcut import shortcut

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

# 버튼 선언
increment = st.button("증가")

# 1. 마우스로 버튼을 누르거나
# 2. 키보드로 스페이스바(space) 또는 엔터(enter)를 누르면 작동
if increment:
    st.session_state.count += 1

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

# --- 키보드 단축키 지정 ---
# 스페이스바나 엔터를 누르면 위의 'increment' 버튼이 실행됩니다.
shortcut(key="space")
shortcut(key="enter")

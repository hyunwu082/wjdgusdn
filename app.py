import streamlit as st

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

# 텍스트 입력창이 비어있지 않으면(아무 키나 눌려서 글자가 들어오면) 숫자 증가
if "typing_box" in st.session_state and st.session_state.typing_box != "":
    # 입력된 글자 수만큼 카운트를 올립니다 (연타 대응)
    st.session_state.count += len(st.session_state.typing_box)
    # 다음 입력을 위해 입력창을 즉시 강제로 비워버립니다
    st.session_state.typing_box = ""
    st.rerun()

st.markdown("### 👇 아래 입력창을 클릭하고 아무 키나 마구 타이핑하세요! (엔터 금지)")

# 글자가 입력되는 순간 바로 반응하는 입력창
st.text_input(
    "여기에 아무 키나 누르기",
    key="typing_box",
    label_visibility="collapsed",
)

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

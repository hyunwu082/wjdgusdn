import streamlit as st

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0


# 입력창에 글자가 바뀌거나 엔터를 누르면 숫자를 올리는 함수
def increment():
    st.session_state.count += 1
    # 입력창을 다시 빈칸으로 초기화하기 위해 세션 스테이트 초기화
    st.session_state.key_input = ""


st.markdown("### 👇 아래 입력창에 아무 키나 치고 [Enter]를 누르세요!")

# 입력창 생성 (글자를 입력하고 엔터를 누르면 무조건 숫자가 올라감)
st.text_input(
    "여기에 아무 키나 누르고 엔터!",
    key="key_input",
    on_change=increment,
    label_visibility="collapsed",
)

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

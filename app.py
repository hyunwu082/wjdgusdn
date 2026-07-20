import streamlit as st

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

# 버튼을 나중에 JavaScript로 클릭할 수 있도록 고유한 Key("increment_btn")를 부여합니다.
if st.button("증가", key="increment_btn"):
    st.session_state.count += 1

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

# --- 스페이스바 입력 감지를 위한 JavaScript 삽입 ---
# 데이터가 변경되어도 포커스를 유지하고, 스페이스바를 누르면 버튼을 클릭하게 만듭니다.
st.components.v1.html(
    """
    <script>
    // 부모 창(Streamlit 앱)의 문서를 가져옵니다.
    const doc = window.parent.document;
    
    // 키다운 이벤트 리스너 추가
    doc.onkeydown = function(e) {
        if (e.keyCode === 32 || e.key === " ") {  // 스페이스바 조건
            e.preventDefault(); // 스페이스바를 눌렀을 때 화면이 아래로 스크롤되는 것을 방지
            
            # 지정한 key를 가진 버튼 요소를 찾아 클릭 이벤트를 발생시킵니다.
            const btn = doc.querySelector("button[aria-label='증가']");
            if (btn) {
                btn.click();
            }
        }
    };
    </script>
    """,
    height=0,  # 화면에 보이지 않도록 높이를 0으로 설정
)

import streamlit as st

st.title("카운터 앱")

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

# 버튼 생성
if st.button("증가"):
    st.session_state.count += 1

st.markdown(f"## 현재 숫자: `{st.session_state.count}`")

# --- 아무 키나 눌러도 버튼이 클릭되게 만드는 JavaScript ---
st.components.v1.html(
    """
    <script>
    const doc = window.parent.document;
    
    // 키보드 아무 키나 눌렸을 때 이벤트 발생
    doc.onkeydown = function(e) {
        // 스페이스바(Space)나 엔터(Enter)의 기본 스크롤/동작 방지
        if (e.key === " " || e.key === "Enter") {
            e.preventDefault();
        }
        
        // '증가' 버튼을 찾아서 클릭 트리거
        const btn = doc.querySelector("button[aria-label='증가']");
        if (btn) {
            btn.click();
        }
    };
    </script>
    """,
    height=0,  # HTML 컴포넌트가 화면을 차지하지 않도록 숨김
)

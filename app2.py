import streamlit as st

from openai import OpenAI
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'user_motto' not in st.session_state:
    st.session_state.user_motto = ""
if 'motto_updated' not in st.session_state:
    st.session_state.motto_updated = False

def add_todo():
    task = st.session_state.todo_input
    if task:
        st.session_state.todo_list.append([task, False])
        st.toast("공부할 개념이 추가되었습니다! ")
        st.session_state.todo_input = ""

@st.dialog("과목 선정")
def edit_motto():
    motto = st.text_input("내가 오늘 공부할 과목을 적어주세요.")
    if st.button("과목 저장"):
        st.session_state.user_motto = motto
        st.session_state.motto_updated = True
        st.rerun()

def page_motto():
    st.header("📣 1. 오늘의 과목")
    st.info(f"개념: {st.session_state.user_motto}")
    if st.button("과목 수정하기"):
        edit_motto()
    if st.session_state.motto_updated:
        st.success("공부할 새로운 과목이 등록되었습니!")
        st.session_state.motto_updated = False
    st.markdown("---")

def page_todo():
    st.header("✅ 2. 모르는 개념")
    st.write(f"현재 다짐: **{st.session_state.user_motto}**")
    new_todo = st.text_input("과목에서 알고 싶은 개념, 모르는 개념을 적으세요.", key="todo_input")
    st.button("추가하기", on_click=add_todo)
    if new_todo == "":
        st.warning("모르는 개념을 입력하고 버튼을 눌러주세요!")
    
    st.markdown("---")
    for i in range(len(st.session_state.todo_list)):
        col_task, col_btn, col_status = st.columns([4, 1, 1])
        with col_task:
            st.write(f"{i+1}. {st.session_state.todo_list[i][0]}")
        with col_btn:
            if st.button("완료", key=f"btn_{i}"):
                st.session_state.todo_list[i][1] = True
                st.rerun()
        with col_status:
            if st.session_state.todo_list[i][1]:
                st.write("✅ **달성!**")
    st.markdown("---")

def page_report():
    st.header("📈 3. 개념 파악 지")
    if not st.session_state.todo_list:
        st.write("아직 등록된 할 일이 없습니다.")
    else:
        total = len(st.session_state.todo_list)
        count = 0
        for item in st.session_state.todo_list:
            if item[1] == True:
                count += 1
        progress = (count / total) * 100
        st.metric("오늘의 달성률", f"{progress:.1f}%")
        st.progress(progress / 100)
        if progress == 100:
            st.balloons()
            st.success("모든 목표를 달성하셨습니다! 🏆")
        if st.button("기록 전체 초기화"):
            st.session_state.todo_list = []
            st.rerun()

def page_ai_coach():
    st.header("🧐 AI 검색창")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            { "role": "system", "content": "너는 사용자의 개념 학습을 도와주는 친절한 AI 튜터야. 이해하기 쉽게 설명하고, 예시와 함께 알려줘."
            }]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("궁금한 개념을 입력하세요."):
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        response = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=st.session_state.messages
        )

        answer = response.choices[0].message.content

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)
    question = st.chat_input("질문을 입력하세요")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            status_context = f"현재 나의 할 일과 달성 여부: {st.session_state.todo_list}"
            prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
            with st.spinner("AI 코치가 생각 중...🤔"):
                response = ai_client.chat.completions.create(
                    model="gpt-5.4-mini",
                    messages=prompt)
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

def page_ai_notion():
    st.header("📖 개념 정리")

    left, right = st.columns([1, 3])

    with left:
        st.subheader("개념")
        st.text_input(
            "개념",
            placeholder="예) 리스트 컴프리헨션",
            label_visibility="collapsed"
        )

    with right:
        st.subheader("정리 내용")
        st.text_area(
            "정리 내용",
            placeholder="AI로부터 찾은 내용을 정리하세요.",
            height=300,
            label_visibility="collapsed"
        )
        if st.button("➕ 추가"):
        st.session_state.concept_count += 1
        st.rerun()

pg = st.navigation([
    st.Page(page_motto, title="오늘의 개념", icon="📣"),
    st.Page(page_todo, title="오늘의 할 일", icon="✅"),
    st.Page(page_report, title="", icon="📈"),
    st.Page(page_ai_coach, title="AI 코칭", icon="🧐"),
    st.Page(page_ai_notion, title="📖 개념 정리")], position="top")
st.title("🕵️개념 확인 노트🕵️")
pg.run()

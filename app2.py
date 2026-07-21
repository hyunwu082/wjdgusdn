import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import re


st.title("📐 방정식 계산기")


st.warning(
    "⚠️ 현재 버전은 y=f(x) 형태의 방정식만 지원합니다.\n\n"
    "예시: y=2*x+1, y=3*cos(x), y=log(x)"
)


x, y = sp.symbols("x y")


# -----------------------
# 초기 상태
# -----------------------

if "equation" not in st.session_state:
    st.session_state.equation = ""

if "last_choice" not in st.session_state:
    st.session_state.last_choice = "직접 입력"

if "reset" not in st.session_state:
    st.session_state.reset = False



# -----------------------
# 예시 방정식 목록
# -----------------------

examples = {
    "직접 입력": "",
    "일차함수 y=2*x+1": "y=2*x+1",
    "이차함수 y=x^2": "y=x^2",
    "삼차함수 y=x^3": "y=x^3",
    "절댓값 함수 y=abs(x)": "y=abs(x)",
    "루트 함수 y=sqrt(x)": "y=sqrt(x)",
    "로그함수 y=log(x)": "y=log(x)",
    "지수함수 y=2^x": "y=2^x",
    "사인 함수 y=sin(x)": "y=sin(x)",
    "코사인 함수 y=cos(x)": "y=cos(x)",
    "탄젠트 함수 y=tan(x)": "y=tan(x)",
    "역비례 함수 y=1/x": "y=1/x",
    "계수 있는 삼각함수 y=3*cos(x)": "y=3*cos(x)"
}



# -----------------------
# 초기화 처리
# -----------------------

if st.session_state.reset:

    st.session_state.equation = ""

    st.session_state.reset = False



# -----------------------
# 보기 선택
# -----------------------

choice = st.selectbox(
    "예시 방정식 선택",
    list(examples.keys())
)



# 선택 변경 감지
if choice != st.session_state.last_choice:

    st.session_state.equation = examples[choice]

    st.session_state.last_choice = choice



# -----------------------
# 입력창
# -----------------------

equation = st.text_input(
    "방정식 입력 (y=f(x) 형태)",
    key="equation"
)



# -----------------------
# 문자 검사
# -----------------------

allowed = "xy0123456789+-*/^=().logsincoqrtab"


for c in equation.replace(" ", ""):

    if c not in allowed:

        st.error(
            "❌ 사용할 수 없는 문자가 있습니다."
        )

        st.stop()



# -----------------------
# x 입력
# -----------------------

x_value = st.number_input(
    "대입할 x 값",
    value=1.0
)



# -----------------------
# 버튼
# -----------------------

col1, col2 = st.columns(2)


with col1:
    calculate = st.button("🧮 계산하기")


with col2:
    reset_button = st.button("🔄 초기화")



# 초기화 버튼
if reset_button:

    st.session_state.reset = True

    st.session_state.last_choice = "직접 입력"

    st.rerun()



# -----------------------
# 계산
# -----------------------

if calculate:

    try:

        if "=" not in equation:

            st.error(
                "❌ = 기호가 필요합니다."
            )

            st.stop()



        left, right = equation.split("=")



        if left.strip() != "y":

            st.error(
                "❌ 현재 버전은 y=f(x) 형태만 지원합니다."
            )

            st.stop()



        # ^ → **
        right = right.replace("^", "**")



        # 3cos(x) → 3*cos(x)
        right = re.sub(
            r"(\d)([a-zA-Z])",
            r"\1*\2",
            right
        )



        expr = sp.sympify(
            right,
            locals={
                "sin": sp.sin,
                "cos": sp.cos,
                "tan": sp.tan,
                "log": sp.log,
                "sqrt": sp.sqrt,
                "abs": sp.Abs
            }
        )



        result = expr.subs(
            x,
            x_value
        )



        st.success(
            f"x={x_value} 일 때 y={result}"
        )



        # -----------------------
        # 그래프
        # -----------------------

        func = sp.lambdify(
            x,
            expr,
            "numpy"
        )


        xs = np.linspace(
            -10,
            10,
            500
        )


        ys = func(xs)



        fig, ax = plt.subplots()


        ax.plot(
            xs,
            ys,
            color="blue",
            label=equation
        )


        ax.scatter(
            [x_value],
            [float(result)],
            color="red",
            label="현재 위치"
        )


        ax.legend()

        ax.grid()

        ax.set_xlabel("x")

        ax.set_ylabel("y")



        st.pyplot(fig)



    except Exception:

        st.error(
            "❌ 방정식을 계산할 수 없습니다."
        )

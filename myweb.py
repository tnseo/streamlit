import streamlit as st

st.set_page_config(
    page_title="선택과목조사",
    page_icon="★")



st.header("2학년 선택과목")


option = st.selectbox("반", range(1,13))
option = st.selectbox("번호", range(1,41))



과목 = st.radio("수강할 과목을 선택해주세요", ("수학1", "수학2", "미적분"))
if 과목 == "수학1":
    st.write("수학1을 선택하셨습니다")
elif 과목 == "수학2":
    st.write("수학2를 선택하셨습니다")
else:
    st.write("미적분을 선택하셨습니다")

과목1 = st.radio("수강할 과목을 선택해주세요", ("물리학1", "화학1", "생물1", "지구1"))
if 과목1 == "물리학1":
    st.write("물리학1을 선택하셨습니다")
elif 과목1 == "화학1":
    st.write("생물1을 선택하셨습니다")
elif 과목1 == "생물1":
    st.write("생물1을 선택하셨습니다")
else:
    st.write("지구1을 선택하셨습니다")


btn = st.button("제출")
if btn:
    st.header("제출 완료")




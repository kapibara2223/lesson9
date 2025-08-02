import streamlit as st
st.title("ユーザー情報入力")
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_grade' not in st.session_state:
    st.session_state.user_grade = ""
if 'user_hobbies' not in st.session_state:
    st.session_state.user_hobbies = []
name = st.text_input("名前")
grade=st.selectbox("学年",
    ["","小学1年", "小学2年", "小学3年", "小学４年","小学5年", "小学6年", "中学1年", "中学2年", "中学3年"])
hobbies=st.text_input("趣味")
if st.button("情報を保存"):
    st.session_state.user_name = name
    st.session_state.user_grade = grade
    st.session_state.user_hobbies = hobbies
    st.success("情報を保存しました!")
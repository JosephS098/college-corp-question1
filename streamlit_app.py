import streamlit as st

st.set_page_config(page_title="QR Code Quiz", page_icon="🧠")

st.title("🧩 Interactive College Corp Quiz")

question = "What is 5 + 3?"
choices = ["6", "7", "8", "9"]
correct_answer = "8"


if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

st.subheader(question)
user_choice = st.radio("Choose your answer:", choices, index=None)


if st.button("Submit"):
    if user_choice == correct_answer:
        st.session_state.answered_correctly = True
        st.success("✅ Correct! Great job!")
    else:
        st.warning("❌ Try again!")


if st.session_state.answered_correctly:
    st.baloons()
    st.info("You can close this quiz or move on to the next QR code!")

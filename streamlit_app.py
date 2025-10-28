import streamlit as st

st.set_page_config(page_title="QR Code Quiz 1", page_icon="🧠")


st.title("🧩 Interactive College Corps Quiz!")
st.markdown("<h3 style='color:#4CAF50;'>Let's see if you can solve this!</h3>", unsafe_allow_html=True)
question = "When was the College Corps Launched?"
choices = ["2019", "2020", "2021", "2022"]
correct_answer = "2021"


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
    st.balloons()
    st.info("You can close this quiz or move on to the next QR code!")

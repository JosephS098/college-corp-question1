import streamlit as st

st.set_page_config(page_title="Quiz Question 1", page_icon="🧠")

st.title("🧩 Interactive Quiz")

# --- Your question here ---
question = "What is 5 + 3?"
choices = ["6", "7", "8", "9"]
correct_answer = "8"

# --- Use Streamlit session state to remember progress ---
if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

st.subheader(question)
user_choice = st.radio("Choose your answer:", choices, index=None)

# Only show feedback when they click the button
if st.button("Submit"):
    if user_choice == correct_answer:
        st.session_state.answered_correctly = True
        st.success("✅ Correct! Great job!")
    else:
        st.warning("❌ Try again!")

# When they finally get it right
if st.session_state.answered_correctly:
    st.balloons()
    st.info("You can close this quiz or move on to the next QR code!")

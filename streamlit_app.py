# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="My Quiz", page_icon="🧠")
st.title("🧠 My Interactive Quiz")

# --- Example structure: replace with your own quiz data/logic ---
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.score = 0
    st.session_state.done = False

# Replace this list with your real questions/answers
questions = [
    {"q": "What is 2 + 2?", "choices": ["3","4","5"], "ans": "4"},
    {"q": "Which is a mammal?", "choices": ["Shark","Dolphin","Eagle"], "ans": "Dolphin"},
]

def show_question(idx):
    q = questions[idx]
    st.subheader(q["q"])
    choice = st.radio("Choose one:", q["choices"], index=None, key=f"q{idx}")
    submitted = st.button("Submit", key=f"submit{idx}", disabled=choice is None)
    if submitted:
        if choice == q["ans"]:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Answer: {q['ans']}")
        st.session_state.i += 1
        st.rerun()

if not st.session_state.done:
    if st.session_state.i < len(questions):
        show_question(st.session_state.i)
    else:
        st.session_state.done = True
        st.rerun()
else:
    st.header("Results")
    st.write(f"Score: **{st.session_state.score}/{len(questions)}**")
    if st.button("Restart"):
        st.session_state.clear()
        st.rerun()

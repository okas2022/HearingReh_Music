
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Auditory Rehab Prototype", layout="centered")

st.title("🎧 Auditory Brain Training: Dual Hemisphere Prototype")
st.markdown("Train your brain with a daily mix of **language** and **music** tasks!")

# Session state for scores
if "language_score" not in st.session_state:
    st.session_state.language_score = 0
if "music_score" not in st.session_state:
    st.session_state.music_score = 0

# --- Language Task ---
st.header("📝 Language Task (Left Brain)")
st.markdown("**Repeat this sentence aloud:**")
sentence = "The quick brown fox jumps over the lazy dog."
st.info(sentence)

if st.button("Simulate STT Evaluation"):
    with st.spinner("Analyzing your speech..."):
        time.sleep(2)
    score = np.random.randint(60, 100)
    st.session_state.language_score = score
    st.success(f"Your language accuracy score: {score}/100")

# --- Music Task ---
st.header("🎵 Music Task (Right Brain)")
st.markdown("**Tap the rhythm by pressing the space bar in sync.**")
st.text("(Simulated here)")

if st.button("Simulate Rhythm Analysis"):
    with st.spinner("Evaluating your rhythm sense..."):
        time.sleep(2)
    score = np.random.randint(60, 100)
    st.session_state.music_score = score
    st.success(f"Your rhythm accuracy score: {score}/100")

# --- Visualization ---
st.header("📊 Brain Balance Score")
labels = ['Language (Left)', 'Music (Right)']
scores = [st.session_state.language_score, st.session_state.music_score]
colors = ['skyblue', 'salmon']

fig, ax = plt.subplots()
ax.bar(labels, scores, color=colors)
ax.set_ylim([0, 100])
ax.set_ylabel("Score")
ax.set_title("Daily Hemisphere Activation")
st.pyplot(fig)

# --- End Message ---
if st.session_state.language_score and st.session_state.music_score:
    avg = (st.session_state.language_score + st.session_state.music_score) / 2
    st.success(f"\nGreat work! Today's brain training average: {avg:.1f}/100")

import streamlit as st
import random
from datetime import date

# --- Page Configuration ---
st.set_page_config(page_title="My Self-Care Hub", page_icon="🌱", layout="centered")

# --- Affirmations List ---
affirmations = [
    "You are capable of amazing things.",
    "It's okay to take a break and recharge.",
    "Your worth is not defined by your productivity.",
    "You're doing the best you can, and that is enough.",
    "Small steps are still progress.",
    "You deserve rest just as much as you deserve success."
]

# --- App Header ---
st.title("🌱 Daily Self-Care Check-In")
st.write(f"**Date:** {date.today().strftime('%B %d, %Y')}")

st.divider()

# --- Section 1: Daily Affirmation ---
st.header("✨ Today's Affirmation")
st.info(random.choice(affirmations))

# --- Section 2: Mental Health Check-In ---
st.header("🧠 Mood Tracker")
mood = st.select_slider(
    "How are you feeling right now?",
    options=["Struggling", "Overwhelmed", "Okay", "Good", "Thriving"],
    value="Okay"
)
st.write(f"Current vibe: **{mood}**")

# --- Section 3: Habit Reminders ---
st.header("✅ Daily Habits")
st.write("Take a second to check off what you've done today:")

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Drank a glass of water")
    st.checkbox("Stepped outside / Got some sun")
with col2:
    st.checkbox("Completed morning/evening skincare routine")
    st.checkbox("Logged a meatless meal")

# --- Section 4: Brain Dump / Journal ---
st.header("📝 Quick Journal")
journal_entry = st.text_area(
    "Get it out of your head and onto the screen:", 
    height=150, 
    placeholder="What's on your mind? No pressure, just write..."
)

# --- Save Button ---
if st.button("Log Today's Check-In"):
    if journal_entry or mood:
        # In the future, we can wire this up to save to a CSV or database!
        st.success("Check-in complete! Proud of you for taking this time today.")
        st.balloons()
    else:
        st.warning("Take a second to reflect before saving!")

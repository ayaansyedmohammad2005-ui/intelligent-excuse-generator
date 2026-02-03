import streamlit as st
import random
import pyttsx3

# ---------------- DATA ---------------- #
excuses = {
    "Work": [
        "My system crashed due to a sudden technical failure.",
        "There was an unexpected client emergency.",
        "I faced a serious network outage."
    ],
    "School": [
        "I was unwell and advised complete rest.",
        "There was a power failure during submission.",
        "A family emergency came up."
    ],
    "Social": [
        "I was stuck in unexpected traffic.",
        "A close friend needed urgent help.",
        "I suddenly felt unwell."
    ]
}

excuse_scores = {
    "Technical issue": 8,
    "Medical emergency": 9,
    "Traffic problem": 6
}

languages = {
    "English": "I had a medical emergency.",
    "Hindi": "मुझे अचानक चिकित्सा आपात स्थिति आ गई थी।"
}

history = []
favorites = []

# ---------------- FUNCTIONS ---------------- #
def generate_excuse(context):
    return random.choice(excuses[context])

def apology(excuse):
    return f"I sincerely apologize for the inconvenience. {excuse}"

def best_excuse():
    return max(excuse_scores, key=excuse_scores.get)

def emergency_msg(name):
    return f"🚨 Urgent! {name} is facing an emergency and may not be reachable."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------------- UI ---------------- #
st.title("🤖 Intelligent Excuse Generator")

context = st.selectbox("Select Scenario", ["Work", "School", "Social"])

if st.button("Generate Excuse"):
    excuse = generate_excuse(context)
    history.append(excuse)
    st.success(excuse)

    if st.button("🔊 Speak Excuse"):
        speak(excuse)

    if st.button("⭐ Add to Favorites"):
        favorites.append(excuse)

st.subheader("🙏 Apology Generator")
if st.button("Generate Apology"):
    if history:
        st.info(apology(history[-1]))
    else:
        st.warning("Generate an excuse first!")

st.subheader("🚨 Emergency Message")
name = st.text_input("Enter Name")
if st.button("Create Emergency Alert"):
    st.error(emergency_msg(name))

st.subheader("🌐 Multi-Language Excuse")
lang = st.selectbox("Choose Language", list(languages.keys()))
st.write(languages[lang])

st.subheader("🏆 Best Ranked Excuse")
st.write(best_excuse())

st.subheader("📜 Excuse History")
st.write(history)

st.subheader("⭐ Favorites")
st.write(favorites)

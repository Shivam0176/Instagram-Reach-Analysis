# app.py
import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model
model = joblib.load("model//model.pkl")

st.set_page_config(page_title="Instagram Reach Simulator", layout="wide")

st.title("🎮 Instagram Reach Simulator")
st.write("Play with engagement metrics and predict your reach!")

# ---------------- UI (GAME CONTROLS) ----------------
col1, col2 = st.columns(2)

with col1:
    likes = st.slider("👍 Likes", 0, 1000, 200)
    saves = st.slider("💾 Saves", 0, 500, 100)
    comments = st.slider("💬 Comments", 0, 100, 10)

with col2:
    shares = st.slider("🔁 Shares", 0, 100, 5)
    profile_visits = st.slider("👤 Profile Visits", 0, 500, 50)
    follows = st.slider("➕ Follows", 0, 200, 20)

# ---------------- PREDICTION ----------------
if st.button("🚀 Simulate Reach"):

    features = np.array([[likes, saves, comments, shares, profile_visits, follows]])
    prediction = model.predict(features)[0]

    # ---------------- OUTPUT ----------------
    st.subheader(f"🔥 Predicted Reach: {int(prediction)}")

    # ---------------- GAME FEEDBACK ----------------
    if prediction < 5000:
        st.warning("📉 Beginner Level")
    elif prediction < 15000:
        st.info("📈 Growing Creator")
    else:
        st.success("🚀 Viral Creator!")

    # ---------------- PROGRESS BAR ----------------
    st.progress(min(int(prediction / 20000 * 100), 100))

    # ---------------- CHARTS ----------------
    st.subheader("📊 Engagement Breakdown")

    data = pd.DataFrame({
        "Metric": ["Likes", "Saves", "Comments", "Shares", "Profile Visits", "Follows"],
        "Values": [likes, saves, comments, shares, profile_visits, follows]
    })

    st.bar_chart(data.set_index("Metric"))

    # ---------------- INSIGHTS ----------------
    st.subheader("🧠 AI Insights")

    if shares > likes * 0.1:
        st.write("✅ Shares are strong → Good for reach!")
    else:
        st.write("⚠️ Increase shares to boost reach")

    if saves > 50:
        st.write("💾 Saves are helping algorithm ranking")

    if comments < 10:
        st.write("💬 Try to increase engagement (ask questions in caption)")

    # ---------------- TARGET MODE ----------------
    st.subheader("🎯 Challenge Mode")
    target = st.number_input("Enter Target Reach", value=10000)

    if prediction >= target:
        st.success("🏆 Target Achieved!")
    else:
        st.error("❌ Try better strategy!")
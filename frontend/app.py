import streamlit as st
import requests
import pandas as pd

# Backend API
API_URL = "http://127.0.0.1:8000/process"

st.set_page_config(page_title="Talent Scout AI", layout="wide")

# -----------------------------
# HEADER
# -----------------------------
st.title("🚀 AI-Powered Talent Scouting & Engagement Agent")
st.markdown("Find, engage, and rank candidates intelligently.")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("⚙️ Settings")
top_k = st.sidebar.slider("Top Candidates", 1, 10, 5)

# -----------------------------
# INPUT
# -----------------------------
st.subheader("📄 Job Description")

jd_text = st.text_area(
    "Paste Job Description:",
    height=150,
    placeholder="Looking for a Python ML Engineer with FastAPI and 3+ years experience..."
)

# -----------------------------
# PROCESS BUTTON
# -----------------------------
if st.button("🔍 Find Candidates"):

    if not jd_text.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Processing candidates..."):

            try:
                response = requests.post(API_URL, json={"jd_text": jd_text})
                data = response.json()

                candidates = data.get("top_candidates", [])[:top_k]

                if not candidates:
                    st.error("No candidates found.")
                else:
                    st.success("✅ Candidates ranked successfully!")

                    # -----------------------------
                    # TABLE VIEW
                    # -----------------------------
                    table_data = []
                    for c in candidates:
                        cand = c["candidate"]
                        table_data.append({
                            "Name": cand["name"],
                            "Experience": cand["experience"],
                            "Match Score": c["match_score"],
                            "Interest Score": c["interest_score"],
                            "Final Score": c["final_score"]
                        })

                    df = pd.DataFrame(table_data)
                    st.subheader("📊 Candidate Overview")
                    st.dataframe(df, use_container_width=True)

                    # -----------------------------
                    # DETAILED VIEW
                    # -----------------------------
                    st.subheader("🔍 Candidate Details")

                    for i, c in enumerate(candidates, 1):
                        cand = c["candidate"]

                        score = c["final_score"]
                        if score > 0.8:
                            status = "🌟 Highly Recommended"
                        elif score > 0.6:
                            status = "✅ Good Fit"
                        else:
                            status = "⚠️ Low Fit"

                        with st.expander(f"{i}. {cand['name']} — {status}"):

                            col1, col2 = st.columns(2)

                            # LEFT
                            with col1:
                                st.markdown("### 👤 Profile")
                                st.write(f"**Experience:** {cand['experience']} years")
                                st.write(f"**Location:** {cand['location']}")
                                st.write(f"**Skills:** {', '.join(cand['skills'])}")
                                st.write(f"**Summary:** {cand['summary']}")

                            # RIGHT
                            with col2:
                                st.markdown("### 📊 Scores")
                                st.metric("Match Score", c["match_score"])
                                st.metric("Interest Score", c["interest_score"])
                                st.metric("Final Score", c["final_score"])

                            # SKILL MATCH
                            st.markdown("### 🧠 Skill Match")
                            st.success("Matched: " + ", ".join(c["explanation"]["matched_skills"]))
                            st.error("Missing: " + ", ".join(c["explanation"]["missing_skills"]))

                            # CONVERSATION
                            st.markdown("### 💬 Candidate Response")
                            st.info(c.get("conversation", "No response available"))

            except Exception as e:
                st.error(f"Error: {e}")
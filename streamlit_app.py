import streamlit as st
from datetime import datetime

# Initialize session state for nav and journal storage
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# Header / Nav
st.markdown("## 🧠 My Streamlit Journal App")
nav = st.radio("Navigate", ["Home", "Dashboard"], horizontal=True)
st.session_state.page = nav
st.divider()

# --- HOME PAGE ---
if st.session_state.page == "Home":
    st.subheader("📚 Journal Entries")

    if not st.session_state.journal_entries:
        st.info("No journal entries yet. Add some from the Dashboard.")
    else:
        for entry in st.session_state.journal_entries[::-1]:  # Show latest first
            with st.container():
                st.markdown(
                    f"""
                    <div style="padding: 1rem; border: 1px solid #ccc; border-radius: 10px; margin-bottom: 10px;">
                        <h4>{entry['date']}</h4>
                        <p>{entry['content']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# --- DASHBOARD PAGE ---
elif st.session_state.page == "Dashboard":
    st.subheader("📋 Dashboard")

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.markdown("### 👤 User Data")
        name = st.text_input("Name", "Juan Dela Cruz")
        email = st.text_input("Email", "juan@example.com")
        mood = st.selectbox("Current Mood", ["😊 Happy", "😐 Okay", "😔 Sad"])

    with col2:
        st.markdown("### 📝 Journal Input")
        journal = st.text_area("Write something...", height=200)

        if st.button("Save Entry"):
            if journal.strip() == "":
                st.warning("Journal entry cannot be empty!")
            else:
                st.session_state.journal_entries.append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "content": journal.strip()
                })
                st.success("Entry saved! Go to Home to view.")
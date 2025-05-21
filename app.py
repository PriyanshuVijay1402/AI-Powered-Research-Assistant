import streamlit as st
from main import crew  # crew is pre-configured with agents and tasks

# Streamlit page configuration
st.set_page_config(page_title="AI Research Assistant", layout="centered")

st.title("📚 AI-Powered Personal Research Assistant")
st.markdown("This assistant finds and summarizes academic research papers from arXiv based on your topic.")

# Input section
user_input = st.text_input("Enter your research topic")

# Button to trigger processing
if st.button("Generate Research Report"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid research topic.")
    else:
        with st.spinner("🔎 Researching... Please wait..."):
            try:
                result = crew.kickoff(inputs={"user_input": user_input})
                st.success("✅ Research Report Generated!")
                st.markdown("### 📝 Final Research Report")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ An error occurred:\n\n{str(e)}")

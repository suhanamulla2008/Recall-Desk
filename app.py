import streamlit as sta

st.set_page_config(
    page_title="RecallDesk",
    page_icon="🧠"
)

st.title("🧠 RecallDesk")
st.subheader("AI Customer Support Assistant")

st.write("Welcome! I'm your AI support assistant.")

message = st.chat_input("Ask your question...")

if message:
    st.chat_message("user").write(message)

    st.chat_message("assistant").write(
        "Hello! I'm RecallDesk. How can I help you?"
    )

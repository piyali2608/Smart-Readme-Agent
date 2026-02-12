import streamlit as st
from agents import get_agent_response

st.set_page_config(page_title="Gemini Agent", page_icon="✨", layout="wide")

# Sidebar for API and Folder Upload
with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("Gemini API Key", type="password")
    
    # Real-life folder uploader
    uploaded_files = st.file_uploader(
        "Upload Project Folder", 
        accept_multiple_files="directory",
        help="Drag and drop your project folder here"
    )

    if uploaded_files:
        st.success(f"Loaded {len(uploaded_files)} files!")

# Initialize Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Generate Project Structure Context from Uploads
folder_context = ""
if uploaded_files:
    structure = [f.name for f in uploaded_files]
    folder_context = "Project Structure:\n" + "\n".join(structure)

# Display Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Interaction
if prompt := st.chat_input("Explain this project or generate a README..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if not api_key:
            st.error("Please add your API Key.")
        else:
            # Gemini-like Thinking process
            with st.spinner("SmartREADME is thinking..."):
                history = [(m["role"], m["content"]) for m in st.session_state.messages[:-1]]
                try:
                    response = get_agent_response(prompt, api_key, history, folder_context)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Download button for generated README
if st.session_state.messages and "###" in st.session_state.messages[-1]["content"]:
    st.download_button("📥 Download README.md", st.session_state.messages[-1]["content"], file_name="README.md")
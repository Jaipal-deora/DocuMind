import requests
import streamlit as st
import os 
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.qdrant_utils import (
    get_all_indexed_files
)

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="DocuMind RAG App",
    layout="wide"
)

# =========================
# Session State
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploading" not in st.session_state:
    st.session_state.uploading = False

# =========================
# Sidebar
# =========================

with st.sidebar:

    st.title("Documents")

    # -------------------------
    # Refresh Documents
    # -------------------------

    try:

        docs_response = requests.get(
            f"{API_URL}/documents"
        )

        all_docs = docs_response.json().get(
            "docs",
            []
        )

    except:
        all_docs = []

    selected_docs = st.multiselect(
        "Select documents",
        options=all_docs,
        default=all_docs
    )

    st.divider()

    # -------------------------
    # Upload File
    # -------------------------

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button(
            "Upload Document",
            disabled=st.session_state.uploading
        ):

            st.session_state.uploading = True

            with st.spinner(
                "Uploading and indexing..."
            ):

                files = {
                    "file": uploaded_file
                }

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

            st.session_state.uploading = False

            if response.status_code == 200:

                st.success(
                    "Uploaded successfully"
                )

                st.rerun()

            else:

                st.error(
                    "Upload failed"
                )

    st.divider()

    # -------------------------
    # Clear Chat
    # -------------------------

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# =========================
# Main Chat UI
# =========================

st.title("RAG Chat Assistant")

# -------------------------
# Display Messages
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =========================
# Chat Input
# =========================

prompt = st.chat_input(
    "Ask something about your documents..."
)

if prompt:

    # -------------------------
    # Add User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -------------------------
    # Assistant Response
    # -------------------------

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""

        try:

            with st.spinner("Thinking..."):

                response = requests.post(
                    f"{API_URL}/chat",
                    params={
                        "query": prompt,
                        "selected_files": selected_docs
                    }
                )

                data = response.json()

                answer = data.get(
                    "response",
                    "No response"
                )

                # Fake streaming effect
                for chunk in answer.split():

                    full_response += chunk + " "

                    response_placeholder.markdown(
                        full_response
                    )

        except Exception as e:

            full_response = str(e)

            response_placeholder.error(
                full_response
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )
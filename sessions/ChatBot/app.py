import streamlit as st
from llm import get_llm
from prompt import get_luffy_prompt

st.set_page_config(page_title="🧢 Luffy Chatbot", page_icon="🏴‍☠️")

st.title("Monkey D. Luffy Chatbot")
st.caption("Talk to Luffy from One Piece")

if "chain" not in st.session_state:
    llm = get_llm()
    prompt = get_luffy_prompt()
    st.session_state.chain = prompt | llm

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

user_input = st.chat_input("Ask Luffy something...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Luffy is thinking..."):
        result = st.session_state.chain.invoke({"user_input": user_input, "history": st.session_state.messages})

    if hasattr(result, "content"):
        response_text = result.content
    else:
        response_text = str(result)

    st.session_state.messages.append(("assistant", response_text))
    with st.chat_message("assistant"):
        st.markdown(response_text)

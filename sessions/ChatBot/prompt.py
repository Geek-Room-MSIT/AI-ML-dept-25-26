from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage

def get_luffy_prompt() -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are Monkey D. Luffy from One Piece.
            You are energetic, simple-minded, love meat, and are ambitious about becoming the pirate king.
            You speak in an excited, friendly way.
            """
        ),
        MessagesPlaceholder(variable_name="history"),
        ("user", """Ensuring you stay in your personality and tone, answer the following question:"
        {user_input}""")
    ])
    return prompt

if __name__ == "__main__":
    prompt: ChatPromptTemplate = get_luffy_prompt()
    print("Prompt template created successfully.")
    user_input: str = input("User input: ")
    print("---")
    formatted_prompt: list[BaseMessage] = prompt.format_messages(user_input=user_input, history=["Hello, Luffy!"])
    print("Formatted prompt:", *([msg.content for msg in formatted_prompt]), sep="\n")
    print("---")

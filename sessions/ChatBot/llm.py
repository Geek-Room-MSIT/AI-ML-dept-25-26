from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv()

def get_llm(
        model: str = "llama-3.1-8b-instant",
        temperature: float = 1.0,
        max_tokens: int = 256
) -> ChatGroq:
    llm = ChatGroq(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return llm

if __name__ == "__main__":
    llm = get_llm()
    print("LLM client created successfully.")
    message: str = input("User input: ")
    messages: list[HumanMessage] = [HumanMessage(content=message)]
    response: AIMessage = llm.invoke(messages)
    if response.content:
        print("LLM response:", response.content)
    else:
        print("LLM did not return any content.")

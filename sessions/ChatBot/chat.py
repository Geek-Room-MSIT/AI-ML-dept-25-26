from llm import get_llm
from prompt import get_luffy_prompt

def main():
    llm = get_llm()
    prompt = get_luffy_prompt()
    print("Welcome to the luffy chatbot")
    print("Exit or quit to end the conversation")
    chain = prompt | llm
    messages = []
    while True:
        uinput = input("You: ")
        messages.append(uinput)
        if uinput.lower() in ["exit", "quit"]:
            print("Luffy: Bye! I'm gonna become the Pirate King!")
            break

        response = chain.invoke({"user_input": uinput, "history": messages})
        print(f"Luffy: {response.content}\n")
        messages.append(response.content)

if __name__ == "__main__":
    main()

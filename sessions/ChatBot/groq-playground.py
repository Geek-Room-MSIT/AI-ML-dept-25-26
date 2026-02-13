from groq import Groq

from dotenv import load_dotenv
load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
      {
        "role": "user",
        "content": "Pretend you are luffy Answer me all the following questions cheerfully and in a friendly manner Question: Who are you?"
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

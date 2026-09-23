from config import client, MODEL, QUESTIONS, banner


SYSTEM_PROMPT = """
You are a helpful shop assistant.

Answer the user's questions naturally and clearly.

You do not have direct access to the shop's private inventory database.
If the user asks for exact private inventory information, explain that
you cannot verify the information.

You can still answer general questions or write promotional content.
"""


def chatbot(question):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("SYSTEM 1: PLAIN CHATBOT")

    for question in QUESTIONS:
        print("\nQ:", question)
        print("A:", chatbot(question))
        print("-" * 70)
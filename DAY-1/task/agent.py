import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are an AI assistant for a small shop.

You have access to private shop inventory through tools.

Never guess private product prices or stock quantities.
Use get_product_price when you need a product price.
Use get_product_stock when you need stock information.
Use calculator whenever arithmetic is required.

Available products:

P101 = Wireless Mouse
P102 = Mechanical Keyboard
P103 = USB-C Hub
P104 = Laptop Stand
P105 = Webcam

If no tool is needed, answer directly.

After receiving tool results, use them to provide a clear final answer.
"""


def agent(question, max_steps=6, verbose=True):

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

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # No tool call means the agent has completed the task
        if not message.tool_calls:
            return message.content.strip()

        # Add assistant tool call to conversation
        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.function.name,
                            "arguments": call.function.arguments
                        }
                    }
                    for call in message.tool_calls
                ]
            }
        )

        # Execute each requested tool
        for call in message.tool_calls:

            name = call.function.name

            # Handles provider-generated extra text after tool name
            clean_name = name.split("<|")[0].strip()

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(clean_name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {clean_name}"

            if verbose:
                print(
                    f"   step {step}: "
                    f"{clean_name}({arguments}) -> {result}"
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                }
            )

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:

        print("\nQ:", question)

        try:
            answer = agent(question)

            print("A:", answer)

        except Exception as e:
            print("Agent error:", e)

        print("-" * 70)
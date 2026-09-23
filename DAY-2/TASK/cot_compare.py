"""Day 2 - New Scenario
Compare Direct Prompting and Chain-of-Thought on an event budget problem.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'DAY-1', 'task')))
from config import client, MODEL, banner


QUESTIONS = [
    # Reasoning question 1
    (
        "A college event has 40 students attending. Snacks cost Rs. 80 "
        "per person, lunch costs Rs. 150 per person, and juice costs "
        "Rs. 40 per person. Decoration costs Rs. 2,500 and a sound system "
        "costs Rs. 4,000. If the club has a budget of Rs. 15,000, "
        "will the budget be enough? If not, how much more is needed?"
    ),

    # Reasoning question 2
    (
        "A college club has 60 students. Each student needs one snack "
        "and one juice. Snacks cost Rs. 75 each and juice costs Rs. 35 each. "
        "The club also pays Rs. 2,000 for decoration. If the budget is "
        "Rs. 10,000, how much money will remain or how much will be needed?"
    ),

    # Logic question
    (
        "Four volunteers—Anu, Bala, Charan and Divya—arrive at an event. "
        "Anu arrives before Bala. Charan arrives after Bala. Divya arrives "
        "before Anu. Who arrived first and who arrived last?"
    ),
]


DIRECT_PROMPT = (
    "You are a helpful assistant. Give only the final answer. "
    "Do not explain."
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem carefully step by step. "
    "Number each step and show the calculation when calculations are needed. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


def ask(system_prompt, question, temperature=0):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("EVENT BUDGET - DIRECT VS CHAIN-OF-THOUGHT")

    for number, question in enumerate(QUESTIONS, start=1):

        print("=" * 80)
        print(f"QUESTION {number}")
        print(question)
        print()

        print("--- WITHOUT CoT ---")
        direct_answer = ask(DIRECT_PROMPT, question)
        print(direct_answer)
        print()

        print("--- WITH CoT ---")
        cot_answer = ask(COT_PROMPT, question)
        print(cot_answer)
        print()
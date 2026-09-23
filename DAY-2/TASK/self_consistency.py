"""Day 2 - Self Consistency for Event Budget Scenario"""

from collections import Counter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'DAY-1', 'task')))
from config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):
    """Extract the Final Answer line from the CoT response."""

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():

            return line.split(":", 1)[-1].strip()

    lines = text.strip().splitlines()

    return lines[-1].strip() if lines else "(empty)"


def run_many(question, runs=RUNS, temperature=TEMPERATURE):

    answers = []

    for attempt in range(1, runs + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": COT_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=temperature,
        )

        answer = final_answer(
            response.choices[0].message.content
        )

        print(f"Run {attempt}: {answer}")

        answers.append(answer)

    return answers


if __name__ == "__main__":

    banner("EVENT BUDGET - SELF CONSISTENCY")

    question = QUESTIONS[0]

    print("QUESTION:")
    print(question)
    print()

    answers = run_many(question)

    winner, count = Counter(answers).most_common(1)[0]

    print()
    print(
        f"Majority answer ({count} of {len(answers)} runs): "
        f"{winner}"
    )
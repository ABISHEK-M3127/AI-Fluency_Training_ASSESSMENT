"""Day 2 - Event Budget ReAct Trace"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'DAY-1', 'task')))
from agent import agent


QUESTION = (
    "A college event has 40 students attending. "
    "The club needs snacks, lunch and juice for everyone. "
    "Snacks cost Rs. 80 per person, lunch costs Rs. 150 per person "
    "and juice costs Rs. 40 per person. "
    "Decoration costs Rs. 2,500 and a sound system costs Rs. 4,000. "
    "The club has a budget of Rs. 15,000. "
    "Will the budget be enough? If not, how much more is needed?"
    "What is the current price of the sound system?"
)


print("QUESTION:")
print(QUESTION)
print()

print("--- REACT AGENT TRACE ---")

answer = agent(
    QUESTION,
    max_steps=10
)

print()
print("--- FINAL ANSWER ---")
print(answer)
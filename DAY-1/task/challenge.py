from agent import agent
from config import banner


CHALLENGE = """
I have ₹4,000. Can I buy a Mechanical Keyboard and a Wireless Mouse?
Calculate the total price and tell me whether I can afford both.
"""


if __name__ == "__main__":

    banner("AGENT CHALLENGE")

    print("Question:")
    print(CHALLENGE)

    print("\nAgent trace:")

    answer = agent(
        CHALLENGE,
        verbose=True
    )

    print("\nFinal Answer:")
    print(answer)
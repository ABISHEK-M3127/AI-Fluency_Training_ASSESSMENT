import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing in .env")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

QUESTIONS = [
    "What is the price of the Mechanical Keyboard?",
    "How much would 3 Wireless Mouse cost?",
    "Which is more expensive, the USB-C Hub or Laptop Stand, and by how much?",
    "Write a short promotional message for the shop's electronics products."
]


def banner(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
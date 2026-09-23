from config import client, MODEL, banner


def main():
    banner("SETUP CHECK")

    print("Provider : Groq")
    print("Model    :", MODEL)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: Setup successful"
                }
            ],
            temperature=0
        )

        print("API Response:", response.choices[0].message.content)
        print("Setup check completed successfully.")

    except Exception as e:
        print("Setup failed.")
        print("Error:", e)


if __name__ == "__main__":
    main()
from config import QUESTIONS, banner


PRODUCTS = {
    "P101": {
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 800,
        "stock": 25
    },
    "P102": {
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 2500,
        "stock": 12
    },
    "P103": {
        "name": "USB-C Hub",
        "category": "Accessories",
        "price": 1200,
        "stock": 18
    },
    "P104": {
        "name": "Laptop Stand",
        "category": "Accessories",
        "price": 1500,
        "stock": 8
    },
    "P105": {
        "name": "Webcam",
        "category": "Electronics",
        "price": 2000,
        "stock": 15
    }
}


def workflow(question):
    q = question.lower()

    # Question 1
    if "price" in q and "mechanical keyboard" in q:
        return "The Mechanical Keyboard costs ₹2,500."

    # Question 2
    if "3" in q and "wireless mouse" in q:
        total = 3 * PRODUCTS["P101"]["price"]
        return f"3 Wireless Mouse cost ₹{total:,}."

    # Question 3
    if "usb-c hub" in q and "laptop stand" in q:
        hub_price = PRODUCTS["P103"]["price"]
        stand_price = PRODUCTS["P104"]["price"]

        difference = abs(stand_price - hub_price)

        if stand_price > hub_price:
            return (
                f"The Laptop Stand is more expensive than the USB-C Hub "
                f"by ₹{difference:,}."
            )
        else:
            return (
                f"The USB-C Hub is more expensive than the Laptop Stand "
                f"by ₹{difference:,}."
            )

    # Question 4
    if "promotional" in q or "electronics products" in q:
        return (
            "Explore our latest electronics collection with useful products "
            "at affordable prices."
        )

    return "Sorry, no predefined rule is available for this question."


if __name__ == "__main__":
    banner("SYSTEM 2: RULE-BASED WORKFLOW")

    for question in QUESTIONS:
        print("\nQ:", question)
        print("A:", workflow(question))
        print("-" * 70)
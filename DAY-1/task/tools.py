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


def get_product_price(product_code):
    product = PRODUCTS.get(product_code)

    if not product:
        return f"Product {product_code} was not found."

    return str(product["price"])


def get_product_stock(product_code):
    product = PRODUCTS.get(product_code)

    if not product:
        return f"Product {product_code} was not found."

    return str(product["stock"])


def calculator(expression):
    """
    Simple calculator for basic arithmetic.

    Only allows numbers and arithmetic operators.
    """

    allowed = set("0123456789+-*/(). ")

    if not all(char in allowed for char in expression):
        return "Invalid expression."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_product_price",
            "description": "Get the private price of a product using its product code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_code": {
                        "type": "string",
                        "description": "Product code such as P101, P102, P103, P104 or P105."
                    }
                },
                "required": ["product_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_stock",
            "description": "Get the current private stock quantity of a product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_code": {
                        "type": "string",
                        "description": "Product code such as P101, P102, P103, P104 or P105."
                    }
                },
                "required": ["product_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Basic arithmetic expression."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


TOOL_FUNCTIONS = {
    "get_product_price": get_product_price,
    "get_product_stock": get_product_stock,
    "calculator": calculator
}
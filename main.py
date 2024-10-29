from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    # HTML with internal CSS for the user interface
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f2f5;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            input[type="number"], select {
                padding: 10px;
                margin: 10px 0;
                width: 80%;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                background-color: #28a745;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 24px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Simple Calculator</h1>
            <form action="/calculate" method="get">
                <input type="number" name="num1" placeholder="Enter first number" required>
                <input type="number" name="num2" placeholder="Enter second number" required>
                <select name="operation" required>
                    <option value="add">+</option>
                    <option value="subtract">−</option>
                    <option value="multiply">×</option>
                    <option value="divide">÷</option>
                </select>
                <button type="submit">Calculate</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, operation: str, num1: float, num2: float):
    # Initialize the result variable
    result = ""
    
    # Perform calculation based on the operation
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "∞"  # Use infinity symbol for divide by zero
    
    # Prepare the HTML response for the result
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculation Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f2f5;
                margin: 0;
            }}
            .container {{
                text-align: center;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }}
            .result {{
                font-size: 24px;
                margin-top: 20px;
                color: #333;
            }}
            .back-button {{
                margin-top: 10px;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                background-color: #007bff;
                color: white;
                cursor: pointer;
            }}
            .back-button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculation Result</h1>
            <div class="result">{num1} {operation_symbol(operation)} {num2} = {result}</div>
            <button class="back-button" onclick="window.history.back()">Back</button>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

def operation_symbol(operation: str) -> str:
    """Returns the symbol corresponding to the operation."""
    if operation == "add":
        return "+"
    elif operation == "subtract":
        return "−"
    elif operation == "multiply":
        return "×"
    elif operation == "divide":
        return "÷"
    return "✘"  # This will never be reached due to validation

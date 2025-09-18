Basic Calculator Project

A Python command-line calculator that supports addition, subtraction, multiplication, and division with proper error handling. This project demonstrates clean, modular code, exception handling, and testing with pytest.

Features

Addition, subtraction, multiplication, and division.

Handles invalid input (non-numeric values).

Prevents division by zero.

Interactive menu for easy user navigation.

Result display after each operation.

Fully tested with pytest.

Installation

Clone this repository:

git clone <your-repo-url>


Navigate to the project folder:

cd basic-calculator


(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies (if any; mostly pytest for testing):

pip install -r requirements.txt

Usage

Run the calculator program:

python calculator.py


You’ll see a menu like:

Basic Calculator
1. Addition
2. Subtract
3. Multiply
4. Divide
5. Exit


Select a number to perform an operation.

Enter the numbers when prompted.

View the result.

Repeat or exit with option 5.

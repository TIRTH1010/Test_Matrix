# Example of list comprehension to create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

import matplotlib.pyplot as plt

# Example data
x = range(10)
y = [x**2 for x in range(10)]

# Create a plot
plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plot of y = x^2')
plt.show()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/squares/{number}")
def read_square(number: int):
    return {"number": number, "square": number**2}

# To run the FastAPI app, use the command: uvicorn new:app --reload
# Example REST API commands:
# GET request to the root endpoint:
# curl -X 'GET' 'http://127.0.0.1:8000/' -H 'accept: application/json'
# GET request to the squares endpoint with a number:
# curl -X 'GET' 'http://127.0.0.1:8000/squares/5' -H 'accept: application/json'
print('New')
print('EOD by eo')
print('My new commit for gitcodespace')

import random

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

if __name__ == "__main__":
    count = 10
    start = 1
    end = 100
    random_numbers = generate_random_numbers(count, start, end)
    print("Random Numbers:", random_numbers)
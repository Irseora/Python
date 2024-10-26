from concurrent.futures import ProcessPoolExecutor
import time

def calc_factorial(number):
    time.sleep(1)
    for i in range(1, number):
        number *= i
    return number

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(calc_factorial, numbers)
        for number, result in zip(numbers, results):
            print(f"Factorial of {number} is {result}")
            
    print(f"Total time taken: {time.time() - start_time}")

if __name__ == "__main__":
    main()
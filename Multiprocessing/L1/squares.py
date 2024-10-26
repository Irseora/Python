from concurrent.futures import ProcessPoolExecutor
import time

def calc_square(number):
    time.sleep(1)
    return number * number

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(calc_square, numbers)
        for number, result in zip(numbers, results):
            print(f"Square of {number} is {result}")

    print(f"Total time taken: {time.time() - start_time}")

if __name__ == "__main__":
    main()
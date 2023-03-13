import time

def slow_sort(numbers: list) -> None:
    # your code here to sort the numbers
    pass

def main() -> None:
    # Uncomment the following line to read from a file.
    # input_file = open('numbers50.txt', 'r')
    # input = input_file.readline
    
    size = int(input())
    numbers = [0] * size
    
    for i in range(size):
        numbers[i] = int(input())
    
    slow_sort(numbers)

    with open(f'output{size}.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number}\n')

if __name__ == '__main__':
    start_time = time.time_ns() / 1000000
    main()    
    end_time = time.time_ns() / 1000000
    
    print(f'Elapsed time: {end_time - start_time} milliseconds.')
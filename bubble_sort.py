import time

class StaticCounter:
    steps = 0

def bubble_sort(numbers: list) -> None:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                StaticCounter.steps += 1

def main() -> None:
    size = int(input())
    numbers = [0] * size
    
    for i in range(size):
        numbers[i] = int(input())
    
    bubble_sort(numbers)

    with open(f'output{size}.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number}\n')

if __name__ == '__main__':
    # start timer in milliseconds
    start_time = time.time_ns() / 1000000
    main()
    
    end_time = time.time_ns() / 1000000
    
    print(f'Elapsed time: {end_time - start_time} milliseconds.')
    print(f'Steps: {StaticCounter.steps}.')
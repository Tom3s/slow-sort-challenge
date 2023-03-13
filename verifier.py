import random

sizes = [50, 1000, 10000] #, 1_000_000]

def verify(size: int) -> None:
    numbers = []
    with open(f'output{size}.txt', 'r') as file:
        numbers = [int(line) for line in file.readlines()]
    
    with open(f'reference{size}.txt', 'r') as file:
        for out_number in numbers:
            ref_number = int(file.readline())
            if out_number != ref_number:
                print(f'Wrong answer for size {size} - {out_number} != {ref_number}')
                return 
    print('OK') 
           
def main() -> None:
    for size in sizes:
        verify(size)

if __name__ == '__main__':
    main()
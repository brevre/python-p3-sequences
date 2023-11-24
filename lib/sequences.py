# lib/sequences.py

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_sequence = [0, 1]
        
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

        print(fibonacci_sequence)

# Uncomment the line below to test the function
# print_fibonacci(9)

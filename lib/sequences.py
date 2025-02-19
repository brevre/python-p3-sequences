def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci = [0, 1] if length > 1 else [0]

    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print(fibonacci)

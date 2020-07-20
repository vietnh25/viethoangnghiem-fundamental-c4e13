def fib( n ):
    if n <= 0: return 0

    fn1 = 1
    fn2 = 1

    for i in range(3, n + 1):
        aux = fn1
        fn1 = fn2 + fn1
        fn2 = aux
    
    return fn1

number = 10

print(f"Fibonacci({number}) => {fib(number)}")
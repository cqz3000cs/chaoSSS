# -*- coding: utf-8 -*-
def fibonacci(n):
    a,b=1,1
    for _ in range(n):
        yield a
        a,b=b,a+b
for fib in fibonacci(10):
    print(fib)
# Sequência a) 1, 3, 5, 7, ___
def proximo_elemento_a():
    return 7 + 2

# Sequência b) 2, 4, 8, 16, 32, 64, ___
def proximo_elemento_b():
    return 64 * 2

# Sequência c) 0, 1, 4, 9, 16, 25, 36, ___
def proximo_elemento_c():
    return 36 + 7 ** 2

# Sequência d) 4, 16, 36, 64, ___
def proximo_elemento_d():
    return 8 ** 2

# Sequência e) 1, 1, 2, 3, 5, 8, ___
def proximo_elemento_e():
    fib = [1, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        if len(fib) >= 7:  # O próximo número será o 7º da sequência Fibonacci
            return next_fib

# Sequência f) 2,10, 12, 16, 17, 18, 19, ___
def proximo_elemento_f():
    return 19 + 1

# Exibindo os próximos elementos
print("Próximos elementos das sequências:")
print("a) ", proximo_elemento_a())
print("b) ", proximo_elemento_b())
print("c) ", proximo_elemento_c())
print("d) ", proximo_elemento_d())
print("e) ", proximo_elemento_e())
print("f) ", proximo_elemento_f())
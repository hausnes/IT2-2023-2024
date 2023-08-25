'''
    Om å optimalisere koden:
    ------------------------
    Me kan bruke timeit-biblioteket for å samanlikne kor lang tid det tek å køyre ulike versjonar av koden vår.
    https://www.geeksforgeeks.org/timeit-python-examples/
    https://docs.python.org/3/library/timeit.html
    Ein problemstilling som kan brukast til å demonstrere korleis me kan optimalisere koden vår er å finne det n-te Fibonacci-tallet.
    https://realpython.com/fibonacci-sequence-python/

'''

from timeit import timeit

kodeFibv1 = '''
# En rekursiv funksjon som finner det n-te Fibonacci-tallet
def fib(n):
    # Basistilfelle: det første og det andre Fibonacci-tallet er 1
    if n == 1 or n == 2:
        return 1
    # Rekursivt kall: det n-te Fibonacci-tallet er summen av de to foregående
    else:
        return fib(n - 1) + fib(n - 2)

# Kaller funksjonen med et eksempelverdi
fib(10)
'''

kodeFibv2 = '''
# En iterativ funksjon som finner det n-te Fibonacci-tallet
def fib_v2(n):
    # Lager to variabler for å holde på de to siste Fibonacci-tallene
    a = 1 # Det første Fibonacci-tallet
    b = 1 # Det andre Fibonacci-tallet
    # Lager en variabel for å holde på det n-te Fibonacci-tallet
    c = a + b # Det tredje Fibonacci-tallet
    # Itererer over tallene fra 4 til n
    for i in range(4, n + 1):
        # Oppdaterer verdiene til de tre variablene ved å skifte dem til høyre
        a = b # Det forrige Fibonacci-tallet blir det nest siste
        b = c # Det nåværende Fibonacci-tallet blir det siste
        c = a + b # Det neste Fibonacci-tallet blir summen av de to siste
    # Returnerer det n-te Fibonacci-tallet
    return c

# Kaller funksjonen med et eksempelverdi
fib_v2(10)
'''

normal_tid:  float = timeit(stmt=kodeFibv1)
optimal_tid: float = timeit(stmt=kodeFibv2)

print(f"Normal tid:  {round(normal_tid, 4)} sekund.")
print(f"Optimal tid: {round(optimal_tid, 4)} sekund.") # denne er rask!
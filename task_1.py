def caching_fibonacci():
    
    cache = {} # порожній словник для кешування

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевірка наявності у кеші
        if n in cache:
            return cache[n]
        # Обчислення та кешування значення
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Bикористання
fib = caching_fibonacci()

print(fib(7))  
print(fib(77))  

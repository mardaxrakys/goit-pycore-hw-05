import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    
    pattern = re.compile(r'\b\d+\.\d+\b') # Регулярний вираз для пошуку дійсних чисел
    for match in pattern.finditer(text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    
    return sum(func(text)) # Генератор для підсумовування чисел

# Використання
text = """
Загальний дохід працівника складається з декількох частин: 
1350.01 як основний дохід, доповнений додатковими надходженнями 39.45 і 570.00 доларів.
"""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

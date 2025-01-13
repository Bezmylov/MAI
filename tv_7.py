from math import factorial
from collections import Counter

def count_permutations(word):
    n = len(word)
    letter_counts = Counter(word)
    denominator = 1
    for count in letter_counts.values():
        denominator *= factorial(count)
    return factorial(n) // denominator

words = ["Безмылов", "Алексей", "АлексейБезмылов"]

for word in words:
    result = count_permutations(word.lower())  # приведение к нижнему регистру для учета одинаковых букв
    print(f"Количество различных слов для '{word}': {result}")
# Реализация алгоритма Кнута-Морриса-Пратта для поиска подстроки в строке
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(text, pattern):
        count = 0
        lps = compute_lps(pattern)
        i = j = 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                count += 1
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return count

    return search(text, pattern)

# Реализация наивного алгоритма для поиска подстроки в строке
def naive_search(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


# Реализация алгоритма Кнута-Морриса-Пратта для поиска подстроки в строке
# (код KMP из предыдущего ответа)

# Генерация простых чисел
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes


# Получение строки из массива простых чисел
primes = generate_primes(500)
primes_str = ' '.join(map(str, primes))

# Поиск наиболее часто встречающихся двузначных чисел в строке с использованием обоих алгоритмов
frequencies_naive = {}
frequencies_kmp = {}

for i in range(len(primes_str) - 1):
    two_digit_num = primes_str[i:i + 2]
    if len(two_digit_num) == 2 and int(two_digit_num) >= 10 and int(two_digit_num) <= 99:
        count_naive = naive_search(primes_str, two_digit_num)
        frequencies_naive[two_digit_num] = count_naive

        count_kmp = kmp_search(primes_str, two_digit_num)
        frequencies_kmp[two_digit_num] = count_kmp

# Наиболее часто встречающиеся двузначные числа и их количество для каждого алгоритма
most_common_naive = max(frequencies_naive.values())
result_naive = [num for num, freq in frequencies_naive.items() if freq == most_common_naive]

most_common_kmp = max(frequencies_kmp.values())
result_kmp = [num for num, freq in frequencies_kmp.items() if freq == most_common_kmp]

# Вывод результата
def print_result():

    print("Наиболее часто встречающиеся двузначные числа и их количество для наивного алгоритма:")
    for num in result_naive:
        print(f"Число: {num}, Количество: {most_common_naive}")

    print("\nНаиболее часто встречающиеся двузначные числа и их количество для алгоритма Кнута-Морриса-Пратта:")
    for num in result_kmp:
        print(f"Число: {num}, Количество: {most_common_kmp}")

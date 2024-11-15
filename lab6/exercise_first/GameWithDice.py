import random
import matplotlib.pyplot as plt

# Подбрасываем кубики и записываем суммы в список
results = []
for _ in range(1350):
    dice_sum = sum(random.randint(1, 6) for _ in range(6000))
    results.append(dice_sum)

# Подсчет количества выпадений каждой возможной суммы
frequency = {}
for result in results:
    if result in frequency:
        frequency[result] += 1
    else:
        frequency[result] = 1

# Вывод графика
def write_graph():
    # Построение графика
    plt.figure(figsize=(10, 8))
    plt.barh(list(frequency.keys()), list(frequency.values()), color='skyblue')
    plt.xlabel('Количество выпадений')
    plt.ylabel('Сумма значений')
    plt.title('Количество выпадений каждой возможной суммы')
    plt.grid(axis='x')
    plt.show()

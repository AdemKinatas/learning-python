# Liste tanımlama
numbers = [1, 2, 3, 4, 5]

# Liste üzerinde döngü kurma
for number in numbers:
    print(number)  # Çıktı: 1 2 3 4 5

numbers.append(6)
print(numbers)  # Çıktı: [1, 2, 3, 4, 5, 6]


def sum_list(list):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [10, 20, 30]
print(sum_list(numbers))  # Çıktı: 60

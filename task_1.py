def find_min_max(arr):
    def helper(left, right):
        # Базовий випадок: один елемент
        if left == right:
            return arr[left], arr[left]

        # Базовий випадок: два елементи
        if left + 1 == right:
            return (min(arr[left], arr[right]), max(arr[left], arr[right]))

        # Рекурсивний випадок: розділення масиву
        mid = (left + right) // 2
        min1, max1 = helper(left, mid)
        min2, max2 = helper(mid + 1, right)

        # Об'єднання результатів
        return min(min1, min2), max(max1, max2)

    if not arr:
        raise ValueError("Масив не може бути порожнім")

    return helper(0, len(arr) - 1)


# Приклад використання
arr = [3, 1, 5, 9, 2, 8, 7, 4, 6, 19999, 4]
print(find_min_max(arr))

import random


def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах довжини масиву")

    def partition(low, high):
        pivot = arr[random.randint(low, high)]  # Випадковий вибір опорного елемента
        left = [x for x in arr[low:high + 1] if x < pivot]
        mid = [x for x in arr[low:high + 1] if x == pivot]
        right = [x for x in arr[low:high + 1] if x > pivot]
        return left, mid, right

    def select(low, high, k):
        left, mid, right = partition(low, high)

        if k <= len(left):
            return select(low, low + len(left) - 1, k)
        elif k <= len(left) + len(mid):
            return mid[0]
        else:
            return select(high - len(right) + 1, high, k - len(left) - len(mid))

    return select(0, len(arr) - 1, k)


# Приклад використання
arr = [3, 1, 5, 9, 2, 8, 7, 4, 6, 111]
k = 4
print(quick_select(arr, k))  # Виведе 4-й найменший елемент

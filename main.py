def read_int_list(prompt: str) -> list[int]:
    while True:
        s = input(prompt).strip()
        try:
            if not s:
                return []
            return list(map(int, s.split()))
        except ValueError:
            print("Ошибка: только целые числа через пробел. Пример: 1 2 -3 4")
def sort_special(arr: list[int]) -> list[int]:
    positives = sorted([x for x in arr if x > 0])
    zeros = [x for x in arr if x == 0]
    negatives = sorted([x for x in arr if x < 0], reverse=True)
    return positives + zeros + negatives
def diff_count(a: list[int], b: list[int]) -> int:
    return len(set(a) ^ set(b))


def process_arrays(a: list[int], b: list[int]):
    d = diff_count(a, b)

    bset = set(b)
    replaced_count = sum(1 for x in a if x not in bset)
    a_replaced = [x if x in bset else 0 for x in a]

    a_sorted = sort_special(a_replaced)
    b_sorted = sort_special(b)

    return d, replaced_count, a_replaced, a_sorted, b_sorted
def main():
    A = read_int_list("Введіть перший масив A : ")
    B = read_int_list("Введіть другий масив B : ")

    print("\nВведені масиви до зміни:")
    print("A:", A)
    print("B:", B)

    print("\nВідсортовані масиви :")
    print("A ↓:", sorted(A, reverse=True))
    print("B ↓:", sorted(B, reverse=True))
    print("A+B ↓:", sorted(A + B, reverse=True))

    d, replaced_count, A_after_replace, A_sorted, B_sorted = process_arrays(A, B)

    print("\nРезультати:")
    print("Кількість неоднакових елементів:", d)

    print("\nA після заміни:")
    print("A':", A_after_replace)

    print("\nA після впорядкування :")
    print("A' sorted:", A_sorted)

    print("\nB після впорядкування :")
    print("B sorted:", B_sorted)
if __name__ == "__main__":
    main()

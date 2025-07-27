from algorithms import *

# Функция для выполнения тестов
def run_tests():
    all_passed = True  # Флаг для отслеживания успешности всех тестов

    # Тесты для функции locate
    test_cases_locate = [
        ([1, 3, 5, 7, 9], 5, (2, 3)),  # Элемент найден
        ([1, 3, 5, 7, 9], 4, (-1, 5)), # Элемент не найден
        ([], 1, (-1, 0)),              # Пустой список
        ([10], 10, (0, 1)),            # Список с одним элементом
    ]

    print("Testing locate...")
    for i, (source, x, expected) in enumerate(test_cases_locate):
        result = locate(source, x)
        if result != expected:
            print(f"Test {i + 1} failed: locate({source}, {x}) -> {result}, expected {expected}")
            all_passed = False
        else:
            print(f"Test {i + 1} passed.")

    # Тесты для функции bin_locate
    test_cases_bin_locate = [
        ([1, 3, 5, 7, 9], 5, (2, 1)),  # Элемент найден
        ([1, 3, 5, 7, 9], 4, (-1, 3)), # Элемент не найден
        ([], 1, (-1, 0)),              # Пустой список
        ([10], 10, (0, 1)),            # Список с одним элементом
    ]

    print("\nTesting bin_locate...")
    for i, (source, x, expected) in enumerate(test_cases_bin_locate):
        result = bin_locate(source, x)
        # Для bin_locate допускаем любое совпадение среди нескольких элементов
        if result[0] == -1 and expected[0] != -1 or result[0] != -1 and source[result[0]] != x or result[1] != expected[1]:
            print(f"Test {i + 1} failed: bin_locate({source}, {x}) -> {result}, expected any match among {expected}")
            all_passed = False
        else:
            print(f"Test {i + 1} passed.")

    # Вывод результата
    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. Please review the errors above.")

# Запуск тестов
if __name__ == "__main__":
    run_tests()

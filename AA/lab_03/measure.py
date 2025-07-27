from algorithms import *
import matplotlib.pyplot as plt

# Функция для создания гистограммы
def create_plot(data, title, xlabel, ylabel, color, label=None):
    plt.bar(range(len(data)), data, color=color, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if label:  # Если указан label, добавляем легенду
        plt.legend()

# Функция для запуска измерений
def run_measure(src):
    # Линейный поиск
    comp = [locate(src, x)[1] for x in src]
    create_plot(comp, "Линейный поиск", "Индекс элемента", "Количество сравнений", color='red', label="Линейный поиск")
    
    # Бинарный поиск
    src_b = sorted(src)  # Сортируем массив для бинарного поиска
    comp_b = [bin_locate(src_b, x)[1] for x in src_b]
    create_plot(comp_b, "Бинарный поиск", "Индекс элемента", "Количество сравнений", color='green', label="Бинарный поиск")
    
    # Показываем график
    plt.show()

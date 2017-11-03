#!/usr/bin/python3

import math
from collections import Counter


def mean(x):
    """Среднее значение"""
    return sum(x) / len(x)


# Медиана - значение, ниже которого расположены 50 % данных
# Квантиль - значение, ниже которого расположен определённый % данных
# Мода - значение или значения, которые встречаются наиболее часто


def median(x):
    """Медиана. Ближайшее к центру число"""
    n = len(x)
    sorted_x = sorted(x)

    mid_point = n // 2

    if n % 2 == 1:
        return sorted_x[mid_point]
    else:
        lo = mid_point - 1
        hi = mid_point
        return (sorted_x[hi] - sorted_x[lo]) / 2


def quantile(x, p):
    """Квантиль"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """Мода"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(x):
    """Размах"""
    return max(x) - min(x)


def de_mean(x):
    """Вектор отклонений от среднего"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """Дисперсия"""
    n = len(x)
    deviations = de_mean(x)
    return sum([x_i ** 2 for x_i in deviations]) / (n - 1)


def standart_deviation(x):
    """Стандартное отклонение"""
    return math.sqrt(variance(x))


def interquartile_range(x):
    """Интерквартильный размах"""
    return quantile(x, 0.75) - quantile(x, 0.25)


# Корреляция - ковариация распределяется между стандартными отклонениями обеих переменных
# Ковариация - измеряет совметное отклонение двух переменных от своих средних
"""
Ковариация
    Когда соотв. элементы векторов х и у оба одновременно выше или ниже своих средних,
    то в сумму входит положительное число. Иначе - отрицательное.
        Большая "положительная" ковариация говорит о:
            х стремится принимать большие значения при больших значениях у
            и малые значения - при малых значениях у
        Большая "отрицательная" означает обратное:
            х стремится принимать малые значения при больших значениях у
            и большие значения - при малых значениях у
        Ковариация близкая к нулю означает, что такой связи не существует

Кореляция
    Интервал (-1, +1) - идеальные антикорреляция и корреляция
    0 - означает отсутствие линейной связи
"""


def dot(x, y):
    return sum([x_i * y_i for x_i, y_i in zip(x, y)])


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    st_dev_x = standart_deviation(x)
    st_dev_y = standart_deviation(y)

    if st_dev_x > 0 and st_dev_y > 0:
        return covariance(x, y) / st_dev_x / st_dev_y
    else:
        return 0


x = [2, 1, 0, 1, 2]
y = [-2, -1, 0, 1, 2]
print(correlation(x, y))

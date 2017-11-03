#!/usr/bin/python3

import math
import random

"""
pdf - probability density function
ДФР - дифференциальная функция распределения
ИФР - интегральная функция распределения

mu - математическое ожидание (среднее значение)
sigma - стандартное откланение
"""


def uniform_pdf(x):
    """
    ДФР равномерного распределения
    """
    return 1 if 0 <= x < 1 else 0


def normal_pdf(x, mu=0, sigma=1):
    """
    ДФР нормального распределения
    """
    return (math.exp((-1) * (x - mu) ** 2 / (2 * sigma ** 2))) / (math.sqrt(2 * math.pi) * sigma)


def normal_cdf(x, mu=0, sigma=1):
    """
    ИФР нормального распределения
    """
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

print(binomial(100, 0.15))

#!/usr/bin/python3

import math
import random


def random_kid():
    return random.choice(['boy', 'girl'])


def boy_girl_paradocs():
    """
    Изветсно, что как минимум одна девочка.
    """
    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)
    for _ in range(10 ** 5):

        younger = random_kid()
        older = random_kid()

        if older == 'girl':  # Старшая?
            older_girl += 1
        if older == 'girl' and younger == 'girl':  # Обе
            both_girls += 1
        if older == 'girl' or younger == 'girl':  # хотя бы одна
            either_girl += 1
    print('P(обе | старшая): ', both_girls / older_girl)
    print('P(обе | любая): ', both_girls / either_girl)


# pdf - probability density function.
#   ДФР - дифференциальная функция распределения
# cdf - cummulative distribution function.
#   ИФР - интегральная функция распределения

def uniform_pdf(x):
    """ДФР равномерного распределения"""
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x):
    """ИФР равномерного распределения"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    """ДФР нормального распределения"""
    return (math.exp(((-1)*(x - mu) ** 2) / 2 / sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)



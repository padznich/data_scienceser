#!/usr/bin/python3
"""
https://people.duke.edu/~ccc14/sta-663/BlackBoxOptimization.html
"""
import os
import sys
import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.linalg as la
from scipy import optimize as opt


plt.style.use('ggplot')


def show_f_plot():

    def f(x):
        return x**3-3*x+1

    x = np.linspace(-3, 3, 100)
    plt.axhline(0)
    plt.plot(x, f(x))

    print(opt.brentq(f, -3, 0), opt.brentq(f, 0, 1), opt.brentq(f, 1, 3))
    print(opt.newton(f, -3), opt.newton(f, 1), opt.newton(f, 3))
    plt.show()


def show_fixed_point():

    def f(x, r):
        """Discrete logistic equation."""
        return r*x*(1-x)

    n = 100
    fps = np.zeros(n)
    x_dots = np.linspace(0, 4, n)
    for i, r in enumerate(x_dots):
        fps[i] = opt.fixed_point(f, 0.5, args=(r, ))

    plt.plot(x_dots, fps)

    plt.show()


def show_convex_function():

    def f(x):
        return (x-4)**2 + x + 1

    with plt.xkcd():
        x = np.linspace(0, 10, 100)

        plt.plot(x, f(x))
        ymin, ymax = plt.ylim()
        plt.axvline(2, ymin, f(2)/ymax, c='red')
        plt.axvline(8, ymin, f(8)/ymax, c='red')
        plt.scatter([4, 4], [f(4), f(2) + ((4-2)/(8-2.))*(f(8)-f(2))],
                     edgecolor=['blue', 'red'], facecolor='none', s=100, linewidth=2)
        plt.plot([2,8], [f(2), f(8)])
        plt.xticks([2,4,8], ('a', 'ta + (1-t)b', 'b'), fontsize=20)
        plt.text(0.2, 40, 'f(ta + (1-t)b) < tf(a) + (1-t)f(b)', fontsize=20)
        plt.xlim([0,10])
        plt.yticks([])
        plt.suptitle('Convex function', fontsize=20)

        plt.show()


def show_minima_plot():

    def f(x, offset):
        return -np.sinc(x - offset)

    x = np.linspace(-20, 20, 100)
    plt.plot(x, f(x, 5))

    # note how additional function arguments are passed in
    sol = opt.minimize_scalar(f, args=(1,))
    print(sol)

    plt.show()

show_minima_plot()

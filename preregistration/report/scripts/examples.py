#!/usr/bin/env python3
#
# Copyright 2018 by Marc Weitz
#
# This script is licensed under the MIT-license.
# See https://opensource.org/licenses/MIT for more information

import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


def seq(start, end, by=0.01):
    return [xx * by for xx in range(int(start / by), int(end / by))]


def plot_polynomial(f, x, c=4):
        y = [f(x_i) for x_i in x]

        if ii == 0:
            plt.plot(x, [y_i - c for y_i in y], ls='-',
                     c="black", label=round(ii, 1))
            plt.plot(x, [y_i + c for y_i in y], ls='-', c="black")
        else:
            plt.plot(x, [y_i - c for y_i in y], ls='--', label=round(ii, 1))


plt.subplot(2, 3, 1)
plt.ylim((-10, 14))
plt.title('$f(x) = a \cdot x + c$')
for ii in seq(-0.5, 0.2, by=0.1):
    plot_polynomial(Polynomial([0., 1. + ii]), seq(0, 4))

plt.subplot(2, 3, 2)
plt.title('$f(x) = a \cdot x^2 + c$')
for ii in seq(-0.5, 0.2, by=0.1):
    plot_polynomial(Polynomial([0., 0., 1. + ii]), seq(0, 4))

plt.subplot(2, 3, 3)
plt.title('$f(x) = a \cdot x^3 + c$')
for ii in seq(-0.5, 0.2, by=0.1):
    plot_polynomial(Polynomial([0., 0., 0., 1. + ii]), seq(0, 4))

lgd = plt.legend(title='$\delta = a - a_{ref}$',
                 bbox_to_anchor=(1.04, 1.04),
                 loc="upper left")
plt.savefig('../plots/examples.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight',
            figsize=(12, 3), dpi=80, transparent=True)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lab import gauss

def peakfit(start, end, angle, count):
    slicedangle, slicedcount = angle[start:end], count[start:end]
    p0 = [max(slicedcount), slicedangle[1], 3]
    coeff, var_matrix = curve_fit(gauss, slicedangle, slicedcount, p0=p0)
    print(np.sqrt(np.diag(var_matrix)))
    return coeff


NaClACE = [
(27, 11, 5),
(27.5, 12, 3),
(28, 23, 3),
(28.5, 33, 3),
(29, 30, 5),
(29.5, 18, 5),
(30, 10, 5),
(30.5, 12, 3),
(31, 47, 5),
(31.5, 83, 7),
(32, 89, 10),
(32.5, 58, 5),
(33, 20, 5),
(33.5, 10, 3),
(34, 10, 3)
]

KClACE = [
(24, 6, 3),
(24.5, 8, 3),
(25, 15, 3),
(25.5, 20, 5),
(26, 18, 3),
(27, 10, 3),
(27.5, 20, 5),
(28, 56, 8),
(28.5, 66, 7),
(29, 45, 3),
(30, 7, 3)
]

RbClACE = [
(23, 8, 3),
(23.5, 14, 4),
(24, 26, 7),
(24.5, 26, 7),
(25, 20, 3),
(25.5, 12, 3),
(26, 25, 5),
(26.5, 68, 7),
(27, 83, 10),
(27.5, 64, 5),
(28, 26, 5),
(28.5, 10, 3),
(29, 7, 5)
]


fig, (naax, kax, rbax) = plt.subplots(3, 1, sharex=True)


for label, ACE, ax, peak in ( ('NaCl', NaClACE, naax, (6, 12)),
                              ('KCl', KClACE, kax, (5, 9)),
                              ('RbCl', RbClACE, rbax, (6, 11))
                            ):
    print label
    angle, count, error = [np.array(_) for _ in zip(*ACE)]
    sortindxs = np.argsort(angle)
    angle, count, error = angle[sortindxs], count[sortindxs], error[sortindxs]
    ax.errorbar(angle, count, xerr=0.25, yerr=error, label=label)

    coeff = peakfit(*peak, angle=angle, count=count)
    fitx = np.linspace(angle[peak[0]], angle[peak[1]], 100)
    ax.plot(fitx, gauss(fitx, *coeff), label='{} fit, center={:03.2f}'.format(label, coeff[1],), linewidth=2, color='r')

    legend = ax.legend(loc='best', shadow=True)
    ax.set_ylabel('count rate, per s')

fig.suptitle('Crystal spacing calculation')
rbax.set_xlabel('angle, 2$\\theta$')
plt.show()

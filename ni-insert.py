import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lab import anglecounterror as no_ni_ACE

# for curve fitting
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

def peakfit(start, end):
    minidx, maxidx = np.argwhere(angle>start)[0], np.argwhere(angle>end)[0]
    slicedangle, slicedcount = angle[minidx:maxidx], count[minidx:maxidx]
    p0 = [max(slicedcount), start, 3]
    coeff, var_matrix = curve_fit(gauss, slicedangle, slicedcount, p0=p0)
    return coeff


anglecounterror = [
(40, 8, 5),
(40.5, 6, 3),
(41, 6, 5),
(41.5, 5, 2),
(42, 4, 3),
(42.5, 5, 2),
(43, 5, 3),
(43.5, 7, 3),
(44, 15, 5),
(44.5, 65, 7),
(45, 88, 7),
(45.5, 68, 5),
(46, 40, 5),
(46.5, 6, 3),
(47, 6, 3),
(47.5, 5, 4),

(85, 2, 1),
(85.5, 3, 2),
(86, 3, 2), # to 89.5
(86.5, 3, 2),
(87, 3, 2),
(87.5, 3, 2),
(88, 3, 2),
(88.5, 3, 2),
(89, 3, 2),
(89.5, 3, 2),

(98, 4, 2),
(98.5, 4, 2),
(99, 5, 3),
(99.5, 10, 3),
(100, 15, 3),
(100.5, 13, 5),
(101, 10, 5),
(101.5, 5, 3),
(102, 3, 2),
]

fig, ax = plt.subplots()


for label, ACE in (('Ni filter', no_ni_ACE), ('Free space', anglecounterror)):
    angle, count, error = [np.array(_) for _ in zip(*ACE)]
    sortindxs = np.argsort(angle)
    angle, count, error = angle[sortindxs], count[sortindxs], error[sortindxs]
    ax.errorbar(angle, np.log(count), xerr=0.25, yerr=error/count, label=label)



legend = ax.legend(loc='upper right', shadow=True)
ax.set_xlabel('angle, 2$\\theta$')
ax.set_ylabel('ln(count rate, per s)')
ax.set_title('LiF bragg peaks')
plt.show()

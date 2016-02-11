import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lab import gauss

def line(x, a, b):
    return a+b*x

a = np.array([10.18, 20.74, 32.04])
b = np.array([9.02, 18.32, 28.2])

lambda_ka = 0.711
lambda_kb = 0.631

a_mult = np.array([1,2,3])*lambda_ka*a
b_mult = np.array([1,2,3])*lambda_kb*b


x = np.concatenate((np.array([1,2,3])*lambda_ka, np.array([1,2,3])*lambda_kb))
y = np.concatenate((np.sin(a*np.pi/180), np.sin(b*np.pi/180)))

popt, pcov = curve_fit(line, x, y)
plt.plot(np.array([1,2,3])*lambda_ka,np.sin(a*np.pi/180), 'bo', label='$K_\\alpha$')

plt.plot(x,y, 'ro', label='$K_\\beta$')

print(popt, np.sqrt(np.diag(pcov)))
print(1/popt[1])
synthx = np.linspace(0.6, 2.6, 100)
plt.plot(synthx, line(synthx, *popt))

plt.ylabel('sin($\\theta$)')
plt.xlabel('n*$\lambda$, Angstroms')
plt.title('Lattice spacing LiF by spacing gradient')
legend = plt.legend(loc='best', shadow=True)

plt.show()

import numpy as np
import math
from matplotlib import pyplot as plot
from matplotlib.animation import FuncAnimation

plot.style.use('seaborn-pastel')

vm = 230
freq = 50
T = 1 / freq
w = 2 * math.pi * freq
t = np.arange(0, 0.1, 0.001)
p = w * t
vs = vm * (np.sin(p))
vo = [0] * len(t)
c = [0] * len(t)
io = [0] * len(t)
pin = [0] * len(t)
E = 150
C = input('Enter 1 if u want to input values: \nEnter 2 if u want to continue with the default one:')
if int(C) == 2:
    R = 100
    alpha = math.pi / 3
else:
    R = float(input('Enter Resistance:'))
    a = float(input('Enter Firing angle(value between 0 to 180):'))
    alpha = (a * math.pi) / 180
    # % To find the minimum triggering angle
theta = math.asin(E / vm)
print("R:", R)
# % output of the Full wave controlled rectifier
n = 0
for i in range(len(t)):
    if float(alpha) < float(theta):
        vo[i] = E
        c[i] = 0
    else:
        if vs[i] > 0:
            if (((2 * n * math.pi) <= w * t[i] < (2 * n * math.pi + float(alpha))) or (
                    w * t[i] > (2 * n * math.pi + math.pi - float(theta)))):
                vo[i] = E
                c[i] = 0
            else:
                vo[i] = vs[i]
                c[i] = (vs[i] - E) / R
        else:
            if ((w * t[i] >= (2 * n * math.pi + float(alpha) + math.pi)) and (
                    w * t[i] < (2 * n * math.pi + 2 * math.pi - float(theta)))):
                vo[i] = -vs[i]
                c[i] = (vs[i] + E) / R
            else:
                vo[i] = E
                c[i] = 0
    if ((w * t[i]) % (2 * math.pi)) == 0 and w * t[i] != 0:
        n = n + 1
    io[i] = (vo[i] - E) / R
    pin[i] = (vs[i]) * (c[i])
# %figure, axes = plot.subplots(nrows=2, ncols=2)

# axes[0, 1].plot(t, vo)

# axes[1, 0].plot(t, c)

# axes[1, 1].plot(t,io)


# figure.tight_layout()
x = t
y1 = vs
y2 = vo
y3 = c
y4 = io
y5 = pin

figure, (a0, a1, a2, a3, a5) = plot.subplots(5, 1)
a0 = plot.subplot(5, 1, 1)
a1 = plot.subplot(5, 1, 2)
a2 = plot.subplot(5, 1, 3)
a3 = plot.subplot(5, 1, 4)
a4 = plot.subplot(5, 1, 5)

data_skip = 10


def init_func():
    # ax.clear()
    a0.set_title('Input Voltage')
    a1.set_title('Output Voltage')
    a2.set_title('Input Current')
    a3.set_title('Output Current')
    a4.set_title('Input Power')
    a0.set_xlabel('time(t)')
    a1.set_xlabel('time(t)')
    a2.set_xlabel('time(t)')
    a3.set_xlabel('time(t)')
    a4.set_xlabel('time(t)')
    a0.set_ylabel('Voltage(V)')
    a1.set_ylabel('Voltage(V)')
    a2.set_ylabel('Current(A)')
    a3.set_ylabel('Current(A)')
    a4.set_ylabel('Watts(W)')

    a0.set_xlim((x[0], x[-1]))
    a1.set_xlim((x[0], x[-1]))
    a2.set_xlim((x[0], x[-1]))
    a3.set_xlim((x[0], x[-1]))
    a4.set_xlim((x[0], x[-1]))
    a0.set_ylim((-max(y1), max(y1)))
    a1.set_ylim((0, max(y2)))
    a2.set_ylim((-max(y3), max(y3)))
    a3.set_ylim((0, max(y4)))
    a4.set_ylim((0, max(y5)))


def update_plot(i):
    a0.plot(x[i:i + data_skip], y1[i:i + data_skip], color='k')
    # ax.scatter(x[i], y[i], marker='o', color='r')
    a1.plot(x[i:i + data_skip], y2[i:i + data_skip], color='k')
    a2.plot(x[i:i + data_skip], y3[i:i + data_skip], color='k')
    a3.plot(x[i:i + data_skip], y4[i:i + data_skip], color='k')
    a4.plot(x[i:i + data_skip], y5[i:i + data_skip], color='k')


anim = FuncAnimation(figure,
                     update_plot,
                     frames=np.arange(0, len(x)),
                     init_func=init_func,
                     interval=20)

figure.tight_layout()

plot.show()

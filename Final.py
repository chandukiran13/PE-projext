import threading
import tkinter as tk
from math import *
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
import pygame


def Average(lst):
    return sum(lst) / len(lst)


def rmsValue(arr):
    n = len(arr)
    square = 0
    mean = 0.0
    root = 0.0
    for i in range(0, n):
        square += (arr[i] ** 2)
    mean = (square / float(n))
    root = sqrt(mean)
    return root


def values():
    window = tk.Tk()
    window.title("Parameters Required")
    tk.Label(window, text="Value of load in Ohms: ").grid(row=0, column=0)
    tk.Label(window, text="Firing angle in Degrees: ").grid(row=1, column=0)
    global e1, e2
    e1 = tk.Entry(window)
    e1.grid(row=0, column=1)
    e2 = tk.Entry(window)
    e2.grid(row=1, column=1)

    def assign():
        global load, delt
        load = int(e1.get())
        delt = (int(e2.get()) * np.pi) / 180

    e3 = tk.Button(window, text="Submit", command=lambda: [assign(), window.destroy()])
    e3.grid(row=2, column=1)
    window.mainloop()


values()

wt = np.arange(0, np.pi * 8, 0.01)  # time array(wt)
Vin = [230 * sin(x) for x in wt]  # Vin
Vout = [0 if (x % (2 * np.pi) < delt or x % (2 * np.pi) > np.pi) else 230 * sin(x) for x in wt]  # Vout
I = [x / load for x in Vout]  # Iin and Iout
Vth = [230 * sin(x) if (x % (2 * np.pi) < delt or x % (2 * np.pi) > np.pi) else 0 for x in wt]  # Vth
Vavg = Average(Vout)
True_power_load = ((rmsValue(Vout)) ** 2) / float(load)
Irms = rmsValue(Vout) / load
Apparent_power = 230 * Irms
if Apparent_power == 0:
    Pf = 0
else:
    Pf = True_power_load / Apparent_power
fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)
pltdata = []
name = ""
title = ""
all_graphs_flag = True
crush = True
pause = False
figVin = fig.add_subplot(4, 1, 1)
figVout = fig.add_subplot(4, 1, 2)
figVth = fig.add_subplot(4, 1, 3)
figI = fig.add_subplot(4, 1, 4)


def mainloop():
    global crush, pltdata, name, title, all_graphs_flag, sub, figI, figVin, figVth, figVout, ani, pause
    while crush:
        gameDisplay.blit(text, textrec)
        gameDisplay.blit(text1, textrec1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crush = False
                ani.event_source.stop()
                plt.close()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                # print(str(x)+"  "+str(y))
                if (550 < x < 710 and 225 < y < 300) and (not all_graphs_flag):
                    all_graphs_flag = True
                    fig.delaxes(sub)
                    figVin = fig.add_subplot(4, 1, 1)
                    figVout = fig.add_subplot(4, 1, 2)
                    figVth = fig.add_subplot(4, 1, 3)
                    figI = fig.add_subplot(4, 1, 4)
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # plt.show()
                if 550 < x < 710 and 300 < y < 370:
                    if not pause:
                        ani.event_source.stop()
                    if pause:
                        ani.event_source.start()
                    pause = not pause
                if 0 < x < 135 and 250 < y < 365:  # Vin
                    if all_graphs_flag:
                        fig.delaxes(figVin)
                        fig.delaxes(figVout)
                        fig.delaxes(figVth)
                        fig.delaxes(figI)
                        sub = fig.add_subplot(1, 1, 1)
                        all_graphs_flag = False
                    pltdata = Vin
                    name = "Vin(V)"
                    title = "Input Voltage"
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # show()
                if 85 < x < 150 and 160 < y < 250:  # In
                    if all_graphs_flag:
                        fig.delaxes(figVin)
                        fig.delaxes(figVout)
                        fig.delaxes(figVth)
                        fig.delaxes(figI)
                        sub = fig.add_subplot(1, 1, 1)
                        all_graphs_flag = False
                    pltdata = I
                    name = "Iin(A)"
                    title = "Input Current"
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # show()
                if 175 < x < 320 and 0 < y < 145:  # Vth
                    if all_graphs_flag:
                        fig.delaxes(figVin)
                        fig.delaxes(figVout)
                        fig.delaxes(figVth)
                        fig.delaxes(figI)
                        sub = fig.add_subplot(1, 1, 1)
                        all_graphs_flag = False
                    pltdata = Vth
                    name = "Vth(V)"
                    title = "Voltage across Thyrister"
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # show()
                if 450 < x < 500 and 110 < y < 170:  # Io
                    if all_graphs_flag:
                        fig.delaxes(figVin)
                        fig.delaxes(figVout)
                        fig.delaxes(figVth)
                        fig.delaxes(figI)
                        sub = fig.add_subplot(1, 1, 1)
                        all_graphs_flag = False
                    pltdata = I
                    name = "Iout(A)"
                    title = "Output current"
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # show()
                if 410 < x < 530 and 240 < y < 320:  # Vo
                    if all_graphs_flag:
                        fig.delaxes(figVin)
                        fig.delaxes(figVout)
                        fig.delaxes(figVth)
                        fig.delaxes(figI)
                        sub = fig.add_subplot(1, 1, 1)
                        all_graphs_flag = False
                    pltdata = Vout
                    name = "Vout(V)"
                    title = "Output Voltage"
                    if pause:
                        clock.tick(50)
                        ani.event_source.start()
                        pause = False
                    # show()
        pygame.display.update()
        clock.tick(30)


def animat(i):
    global pltdata, name, title, all_graphs_flag, Vin, Vout, Vth, I
    if not all_graphs_flag:
        sub.clear()
        ymax = max(abs(max(pltdata)), abs(min(pltdata)))
        sub.set_ylim([-1.2 * ymax, 1.2 * ymax])
        sub.plot(wt, pltdata)
        sub.set_xlim([0, 8 * np.pi])
        sub.grid(True)
        sub.set_title(title)
        sub.set_xlabel("wt")
        sub.set_ylabel(name)
        pltdata = [pltdata[(i - 10) % len(pltdata)] for i, x in enumerate(pltdata)]
    else:
        figVin.clear()
        figVout.clear()
        figVth.clear()
        figI.clear()
        figVin.grid(True)
        figVout.grid(True)
        figVth.grid(True)
        figI.grid(True)
        figVin.plot(wt, Vin, c="r", label="Vin")
        figVout.plot(wt, Vout, c="g", label="Vout")
        figVth.plot(wt, Vth, c="y", label="Vth")
        figI.plot(wt, I, label="I")
        figVin.set_ylabel("Vin(V)")
        figVin.set_title("Input Voltage")
        ymax = max(abs(max(Vin)), abs(min(Vin)))
        if ymax == 0:
            figVin.set_ylim([-1.2 * ymax - 0.1, 1.2 * ymax + 0.1])
        else:
            figVin.set_ylim([-1.2 * ymax, 1.2 * ymax])
        figVin.set_xlim([0, 8 * np.pi])
        figVin.legend()
        figVout.set_ylabel("Vout(V)")
        figVout.set_title("Output Voltage")
        ymax = max(abs(max(Vout)), abs(min(Vout)))
        if ymax == 0:
            figVout.set_ylim([-1.2 * ymax - 0.1, 1.2 * ymax + 0.1])
        else:
            figVout.set_ylim([-1.2 * ymax, 1.2 * ymax])
        figVout.set_xlim([0, 8 * np.pi])
        figVout.legend()
        figVth.set_ylabel("Vth(V)")
        figVth.set_title("Voltage across Thyristor")
        ymax = max(abs(max(Vth)), abs(min(Vth)))
        if ymax == 0:
            figVth.set_ylim([-1.2 * ymax - 0.1, 1.2 * ymax + 0.1])
        else:
            figVth.set_ylim([-1.2 * ymax, 1.2 * ymax])
        figVth.set_xlim([0, 8 * np.pi])
        figVth.legend()
        figI.set_ylabel("I(A)")
        figI.set_title("Current")
        ymax = max(abs(max(I)), abs(min(I)))
        if ymax == 0:
            figI.set_ylim([-1.2 * ymax - 0.1, 1.2 * ymax + 0.1])
        else:
            figI.set_ylim([-1.2 * ymax, 1.2 * ymax])
        figI.set_xlim([0, 8 * np.pi])
        figI.legend()
        Vin = [Vin[(i - 20) % len(Vin)] for i, x in enumerate(Vin)]
        Vth = [Vth[(i - 20) % len(Vth)] for i, x in enumerate(Vth)]
        Vout = [Vout[(i - 20) % len(Vout)] for i, x in enumerate(Vout)]
        I = [I[(i - 20) % len(I)] for i, x in enumerate(I)]


pygame.init()
image = pygame.image.load("question.png")
imgsize = image.get_size()
gameDisplay = pygame.display.set_mode(imgsize)
pygame.display.set_caption("Thyristor Circuit")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 25)
text = font.render("Voavg = " + str(Vavg)[:5] + 'V', True, (0, 0, 0), (255, 255, 255))
text1 = font.render("Power Factor =" + str(Pf)[:5], True, (0, 0, 0), (255, 255, 255))
textrec = text.get_rect()
textrec1 = text1.get_rect()
textrec.center = (610, 60)
textrec1.center = (600, 100)
gameDisplay.blit(image, (0, 0))
plt.delaxes(sub)
main_t = threading.Thread(target=mainloop, args=())
main_t.start()
ani = anim.FuncAnimation(fig, animat, interval=50)
plt.show()
crush = False
pygame.quit()
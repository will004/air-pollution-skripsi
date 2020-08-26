from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')


class Canvas3D(Canvas):
    def __init__(self):
        self.fig = plt.figure()
        Canvas.__init__(self, self.fig)
        self.axes = self.fig.gca(projection='3d')

    def drawGraph(self, x, t, C):  # Fun for Graph plotting
        x, t = np.meshgrid(x, t)
        self.axes.clear()
        # plots the 3D surface plot
        self.axes.plot_surface(x, t, C, cmap='jet')
        self.axes.set_xlabel('Space (cm)')
        self.axes.set_ylabel('Time (s)')
        self.axes.set_zlabel('Concentration')
        self.draw_idle()


class Canvas2D(Canvas):
    def __init__(self):
        self.fig = plt.figure(tight_layout=True)
        Canvas.__init__(self, self.fig)  # creating FigureCanvas
        self.axes = self.fig.gca()

    def drawGraph(self, x, t, C, userTimeInput=list()):
        self.axes.clear()

        if userTimeInput:
            userInput = list(userTimeInput)
            idx_userInput = 0
            counter = 0
            colCount = 4
            for idx, n in enumerate(t):
                if t[idx] == userInput[idx_userInput]:
                    self.axes.plot(x, C[idx, :], label=f'$t={int(t[idx])}\ s$')
                    idx_userInput += 1
                    counter += 1
                if idx_userInput == len(userInput):
                    break
            if counter//colCount == 0:
                counter = colCount
            if len(userInput) <= 12:
                self.axes.legend(
                    prop={'size': 6}, loc='upper left', bbox_to_anchor=(1.04, 1))
            elif len(userInput) > 12:
                self.axes.legend(
                    ncol=counter//colCount, prop={'size': 6}, loc='lower right', bbox_to_anchor=(1, 0))

        else:
            counter = 0
            for idx, n in enumerate(t):
                if t[idx] % 1 == 0 and t[idx] > 0:
                    self.axes.plot(x, C[idx, :], label=f'$t={int(t[idx])}\ s$')
                    counter += 1
            if counter//5 == 0:
                counter = 5
            if counter <= 6:
                self.axes.legend(ncol=counter//5)
        self.axes.set_xlabel('Space (cm)')
        self.axes.set_ylabel('Time (s)')
        self.draw_idle()

    def clearGraph(self):
        self.axes.clear()
        self.draw_idle()

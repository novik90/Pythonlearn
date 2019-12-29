#import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import numpy as np

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = '/Users/novik90/Desktop/Pythonlearn/matplotlib/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt))
    os.chdir(pwd)


def figure_1():
    fig = plt.figure()
    print(fig.axes)
    print(type(fig))
    plt.scatter(1.0, 1.0)
    plt.scatter(2.0, 0.5)
    print(fig.axes)

    save(name='pic_1', fmt='png')

    plt.show()
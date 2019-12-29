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

def figure_2():
    fig = plt.figure()
    print('create figure ', fig)
    ax = fig.add_axes([0, 0, 1, 1])
    plt.scatter(0.0, 0.5)
    plt.savefig('example 142a.png', fmt='png')

    fig = plt.figure()
    print('create figure ', fig)
    ax = fig.add_axes([0, 0, 1, 1], polar=True)
    plt.scatter(0.0, 0.5)
    plt.savefig('example 142b.png', fmt='png')

    save('pic_1_4_2', fmt='png')

    plt.show()

def figure_3():
    lag = 0.1
    x = np.arange(0.0, 2*np.pi+lag, lag)
    y = np.sin(x)
    fig = plt.figure()
    plt.plot(x, y)

    plt.grid(True)

    save('pic_1_5_1', fmt='png')

    plt.show()

figure_3()
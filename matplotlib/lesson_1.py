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

def figure_4():
    N = 100
    n = np.sqrt(N)
    x = np.arange(n)
    z = np.random.random(N).reshape(n, n)
    y = z[5,:]

    fig = plt.figure()
    cc = plt.contourf(z, alpha=0.5)
    plt.plot(x, y, label='line', color='red')

    plt.title('1a. Title')
    plt.xlabel('2a. Xlabel')
    plt.ylabel('3a. Ylabel')
    plt.legend()
    cbar = plt.colorbar(cc)

    plt.text(2.5, 7, '1. Axes', fontsize=26, bbox=dict(edgecolor='w', color='w'))
    plt.text(4, -0.5, '2. XAxis', fontsize=18, bbox=dict(edgecolor='w', color='w'))
    plt.text(-0.5, 3.8, '3. YAxis', fontsize=18, bbox=dict(edgecolor='w', color='w'), rotation=90)
    plt.text(6.3, 7.2, '4. Legend', fontsize=16, bbox=dict(edgecolor='w', color='w'))
    plt.text(9.1, 5., '5. Colorbar', fontsize=16, bbox=dict(edgecolor='w', color='w'), rotation=90)
    plt.text(7., 0.8, '6. Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))
    plt.text(0.8, 8.4, '7. Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)

    cbar.ax.set_xlabel('5a. Colorbar Xlabel', color='k', rotation=30)
    cbar.ax.set_ylabel('5b. Colorbar Ylabel', color='k')

    plt.text(2.8, 4.8,'6. Grid lines', fontsize=14)
    plt.grid(True)

    save('pic_1_5_2', fmt='png')

    plt.show()

figure_4()
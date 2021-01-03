'''
由于我的animation在jupyter notebook中不能正确跑出，这里用.py文件运行
'''

from Life import Life, LifeViewer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import thinkplot


rc('animation', html='html5')

def make_viewer(n, m, row, col, *strings):
    """Makes a Life and LifeViewer object.
    n, m: rows and columns of the Life array 
    row, col: upper left coordinate of the cells to be added   
    strings: list of strings of '0' and '1'
    """
    life = Life(n, m)   # n行m列的格子
    life.add_cells(row, col, *strings)   # 左上角坐标
    viewer = LifeViewer(life)   # 瞅一眼
    return viewer


def main1():
    puffer_train1 = [
        '0000000001111', 
        '0000000010001',
        '0000000000001',
        '0000000010010',
        '0000000000000', 
        '0000000000000',
        '0000000011000',
        '0110000100100',
        '1010000100100',
        '0010001101100',
        '0000000110000',
        '0000000000000', 
        '0000000000000',
        '0000000000000',
        '0000000001111',
        '0000000010001',
        '0000000000001',
        '0000000010010'
    ]
    viewer = make_viewer(40, 100, 11, 1, *puffer_train1)
    anim = viewer.animate(frames=400, interval=50, grid=True)
    plt.show()

def main2():
    puffer_train2 = [
        '011100000000000111', 
        '100100000000001001', 
        '000100001110000001', 
        '000100001001000001',
        '001000010000000010'
    ]
    viewer = make_viewer(100, 30, 90, 5, *puffer_train2)
    anim = viewer.animate(frames=400, interval=50, grid=True)
    plt.show()


if __name__ == '__main__':
    # 这里生成动画的速度可能比较慢
    main1()
    main2()

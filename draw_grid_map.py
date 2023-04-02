import numpy as np
import matplotlib.pyplot as plt

def draw_grid_map(data):
    # グリッドマップのサイズ取得
    row, col = data.shape

    # ウィンドウのサイズを指定
    plt.figure(figsize=(col/2, row/2))

    # マップのデータを画像として表示
    plt.imshow(data, cmap='gray')

    # 格子状の線を描画
    plt.grid(which='major', color='black', linestyle='-', linewidth=1)

    # 軸を設定
    plt.xticks(np.arange(-0.5, col, 1))
    plt.yticks(np.arange(-0.5, row, 1))
    plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

    # グラフを表示
    plt.show()
    

if __name__ == '__main__':
    # グリッドマップのデータ（1: 何もなし、0: 障害物）
    grid_map = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ])
    
    # グリッドマップを描画
    draw_grid_map(grid_map)

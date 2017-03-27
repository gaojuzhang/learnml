#!/usr/bin/python
# _*_ coding : utf-8 _*_

import pandas as pd

def run_main():
    csv_path =  'Advertising.csv'
    # pandas 读取数据
    data = pd.read_csv(csv_path)

    x = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']

    # 绘制1
    plt.plot

if __name__ == '__main__':
    run_main()
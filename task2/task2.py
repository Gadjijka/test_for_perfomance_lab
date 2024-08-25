import argparse
import os
import math


def arg_parser():
    parser = argparse.ArgumentParser(
        description='''Напишите программу, которая рассчитывает
            положение точки относительно окружности.
            Координаты центра окружности и его радиус,
            также как и координаты точек, считываются из файла.
            Ответ 0 - точка лежит на окружности,
            1 - точка внутри окружности, 2 - точка снаружи
    ''')
    parser.add_argument('file_path_1', type=str, help='''Координаты центра окружности
        и его окружности''')
    parser.add_argument('file_path_2', type=str, help='Координаты точек')
    return parser.parse_args()

def loading_circle(file_path_1):
    circle = {}
    with open(file_path_1, 'r') as f:
        circle['centre'] = f.readline().replace('\n', '')
        circle['radius'] = f.readline(2).replace('\n', '')
    return circle

def unloading_the_file_with_dots(circle, file_path_2):
    with open(file_path_2, 'r') as f:
        for line in f:
            print(checking_the_location_of_dot(line.replace('\n', ''), circle))

def checking_the_location_of_dot(dot, circle):
    result = math.sqrt((int(dot[0]) - int(circle['centre'][0]))**2 + (int(dot[2]) - int(circle['centre'][2]))**2)
    if result < int(circle['radius']): return 1
    if result == int(circle['radius']): return 0
    if result > int(circle['radius']): return 2

def main():
    args = arg_parser()
    circle = loading_circle(args.file_path_1)
    unloading_the_file_with_dots(circle, args.file_path_2)

if __name__ == "__main__":
    main()

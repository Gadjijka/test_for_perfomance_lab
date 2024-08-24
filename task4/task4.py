import argparse
import os

def arg_parser():
    parser = argparse.ArgumentParser(
        description='''Дан массив целых чисел nums.
            Напишите программу, выводящую минимальное количество ходов, требуемых для
            приведения всех элементов к одному числу.
            За один ход можно уменьшить или увеличить число массива на 1.
    ''')
    parser.add_argument('file_path', type=str, help='Файл с числами')
    return parser.parse_args()

def unload_file(file_path):
    massive = []
    with open(file_path) as f:
        for line in f:
            massive.append(int(line.replace('\n', '')))
    return massive

def define_amount_turns(massive):
####Та точка, от которой минимизирует количество ходов
####для приведения элементов массива к одному числу
    m = 0
    m = len(massive) // 2
    sum = 0
    for i in massive:
        sum += abs(i - massive[m])
    return sum

if __name__ == '__main__':
    args = arg_parser()
    massive = unload_file(args.file_path)
    print(define_amount_turns(sorted(massive)))

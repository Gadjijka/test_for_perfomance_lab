import argparse


def arg_parser():
    parser = argparse.ArgumentParser(
        description='''Круговой массив - массив из элементов,
            в котором по достижению конца массива
            следующим элементом будет снова первый.
            Массив задается числом n, то есть
            представляет собой числа от 1 до n.
            Напишите программу, которая выводит путь,
            по которому, двигаясь интервалом длины
            m по заданному массиву, концом будет являться первый элемент.
            Началом одного интервала является конец предыдущего.
            Путь - массив из начальных элементов полученных интервалов.
    ''')
    parser.add_argument('n', type=int, help='Массив чисел от 1 до n')
    parser.add_argument('m', type=int, help='''Длина интервала m,
        по которому вы двигаетесь по массиву''')
    return parser.parse_args()

def regulate_value_m(n, m):
    if m > n:
        if m % n == 0:
            return n
        else:
            return m % n
    return m

def the_main_logic(n, m):
    massive = [x for x in range(1, n+1)]
    road = ''
####Переменная, которая будет сравниваться с m, если оно будет равно этой
####Переменной и символ оканчивающийся приэтой итерации будет равен начальному,
####То выходим из цикла
    index_for_m = 0
    i = 0
####Здесь регулируем значение m если оно больше размера зданного массива
    m = regulate_value_m(n, m)
    s = ''
    while True:
        if index_for_m == m - 1:
            road += s[0]
            if massive[i] == massive[0]:
                break
            index_for_m = 0
            s = ''
        s += str(massive[i])
        if i == len(massive) - 1:
            i = 0
        else:
            i += 1
        index_for_m += 1
    print(f'The whole path - {road}')

def main():
    args = arg_parser()
    the_main_logic(args.n, args.m)

if __name__ == "__main__":
    main()

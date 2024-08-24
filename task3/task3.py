import argparse
import os
import json

def arg_parser():
    parser = argparse.ArgumentParser(
        description='''На вход в качестве аргументов программы поступают три пути к файлу.
            values.json содержит результаты прохождения тестов с уникальными id
            tests.json содержит структуру для построения отчета на основе прошедших
            тестов (вложенность может быть большей, чем в примере)
            report.json - сюда записывается результат
            Напишите программу, которая формирует файл report.json с заполненными полями
            value для структуры tests.json на основании values.json.
    ''')
    parser.add_argument('file_path_1', type=str, help='values.json')
    parser.add_argument('file_path_2', type=str, help='tests.json')
    parser.add_argument('file_path_3', type=str, help='report.json')
    return parser.parse_args()

def unload_file_json(file_path):
    data = {}
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def report_file(values_json, tests_json, file_path):
    for key in tests_json.keys():
        

if __name__ == "__main__":
    args = arg_parser()
    values = unload_file_json(args.file_path_1)
    tests = unload_file_json(args.file_path_2)
    report_file(values, tests, arg.file_path_3)

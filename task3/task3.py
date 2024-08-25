import argparse
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

def fill_report(test_data, value_data):
    for test in test_data:
        print(test)
        if 'id' in test:
            test_id = test['id']
            if test_id in value_data:
                test['value'] = value_data[test_id]
        if 'children' in test:
            print(test)
            fill_report(test['children'], value_data)


def write_file(file, file_path):
    with open(file_path, 'w') as write:
        json.dumps(file, indent=4)

def main():
    

if __name__ == "__main__":
    args = arg_parser()
    values = unload_file_json(args.file_path_1)
    tests = unload_file_json(args.file_path_2)
    fill_report(tests, values['values'])
    write_file(tests, args.file_path_3)

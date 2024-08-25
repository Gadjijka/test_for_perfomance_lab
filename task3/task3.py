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
    for key in test_data.keys():
        if isinstance(test_data[key], dict):
            fill_report(test_data[key], value_data)
        for i in value_data:
            for i1 in i:
                print(key['id'], i1['id'])
                if key['id'] == i1['id']:
                    key['value'] = i1['value']


def write_file(file, file_path):
    print(file)
    with open(file_path, 'w') as write:
        json.dumps(file, indent=4)

def main():
    args = arg_parser()
    values = unload_file_json(args.file_path_1)
    tests = unload_file_json(args.file_path_2)
    fill_report(tests, values['values'])
    write_file(tests, args.file_path_3)

if __name__ == "__main__":
    main()

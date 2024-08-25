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

def fill_report(tests_structure, values):
    if isinstance(tests_structure, dict):
        for key, value in tests_structure.items():
            if key == 'id':
                for i in values['values']:
                    if i['id'] == value:
                        tests_structure['value'] = i['value']
            elif isinstance(value, dict) or isinstance(value, list):
                fill_report(value, values)
    elif isinstance(tests_structure, list):
        for item in tests_structure:
            fill_report(item, values)

def write_file(file, file_path):
    print(file)
    with open(file_path, 'w') as write:
        json.dump(file, write, indent=4)

def main():
    args = arg_parser()
    values = unload_file_json(args.file_path_1)
    tests = unload_file_json(args.file_path_2)
    fill_report(tests, values)
    write_file(tests, args.file_path_3)

if __name__ == "__main__":
    main()

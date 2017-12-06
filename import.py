import argparse
from os import path
import re
import csv
from database import Database

parser = argparse.ArgumentParser(
                description='Import Source engine files to another format or \
                                convert them into csv.')
parser.add_argument('-v',
                    '--verbose',
                    help="be more verbose",
                    action="store_true")

parser.add_argument('-f',
                    '--format',
                    help="set output file format",
                    type=str,
                    choices=['csv', 'sql'])

parser.add_argument('-o',
                    '--output',
                    help="set output file name",
                    type=str)

parser.add_argument('-i',
                    '--input',
                    help="set input file name",
                    nargs='+',
                    type=argparse.FileType('r'))

args = parser.parse_args()


verbose = True if args.verbose else False
format = args.format if args.format else 'csv'


def parce_source(files):
    total_tokens = 0
    data = {}
    for file in files:
        file_name = path.splitext(path.basename(file.name))[0]
        log(f'Processing {file_name} to {format}')
        try:
            with open(file.name, encoding='utf-16') as file:
                source_file = file.read()
        except UnicodeDecodeError:
            with open(file.name, encoding='utf-8') as file:
                source_file = file.read()
        pattern = re.compile(
            r'\"(?P<indentifactor>.*?)\".*?\"(?P<translation>.*)\"\n'
            r'\"\[english].*?\".*?\"(?P<original>.*)\"', re.MULTILINE)
        match = pattern.findall(source_file)
        total_tokens += len(match)
        log(f'Found {len(match)} tokens')
        data[file_name] = [match]
    log(f'Total number of tokens: {total_tokens}')
    return data


def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter='\t',
                            quotechar='|',
                            quoting=csv.QUOTE_ALL)
        writer.writerow(['Індентифікатор токена', 'Переклад', 'Оригінал'])
        for file in data.keys():
            for row in data[file]:
                for match in row:
                    writer.writerow(match)


def write_db(data):
        db = Database()
        for file in data.keys():
            for row in data[file]:
                for match in row:
                    (key, translation, original) = match
                    db.add_token(key, file, original, translation)
                    log(f'Add {key}')
                db.commit()


def log(phrase):
    if verbose:
        print(phrase)


if args.input:
    data = parce_source(args.input)
    if format == 'csv':
        filename = args.output if args.output else 'output.csv'
        write_csv(filename, data)
    elif format == 'sql':
        write_db(data)

import argparse
from database import Database

parser = argparse.ArgumentParser(
                description="Export tokens into Source engine's format.")

parser.add_argument('-v',
                    '--verbose',
                    help="be more verbose",
                    action="store_true")

parser.add_argument('-b',
                    '--branch',
                    help="set branch for output",
                    type=str)

args = parser.parse_args()


verbose = True if args.verbose else False


def log(phrase):
    if verbose:
        print(phrase)


if args.branch:
    branch = args.branch
    db = Database()
    tokens = db.get_branch(branch)
    for lang in ['english', 'ukrainian']:
        with open(f'{branch}.txt', 'w') as file:
            file.write('"lang"\n')
            file.write('{\n'+f'"Language" "{lang.capitalize()}"'+'\n')
            file.write('"Tokens"\n{\n')
            for token in tokens:
                file.write(f'"{token.key}"'+'\t'+f'"{token.original}"'+'\n')
                file.write(f'"{token.key}"'+'\t'+f'"{token.translation}"'+'\n')
            file.write('}\n}')

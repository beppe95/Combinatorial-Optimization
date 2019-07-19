from pathlib import Path


def read_file(problem_name):
    p = Path(problem_name).resolve()

    with open(p, encoding='utf-8') as input_file:
        lines = input_file.readlines()
        # gestire l'header del file
        for line in lines[6:]:
            print(line)
            # gestire i nodi su ogni riga {id, x, y}

def read_opt_file(problem_name):
    p = Path(problem_name).resolve()

    with open(p, encoding='utf-8') as input_file:
        lines = input_file.readlines()
        # gestire l'header del file
        for line in lines[5:]:
            print(line)
            # gestire la lista dei nodi del tour
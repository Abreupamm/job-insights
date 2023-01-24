from src.pre_built.sorting import sort_by

jobs_list = [
    {"salary": "2000", "title": "Maquinista", "type": "trainee"},
    {"salary": "3000", "title": "Motorista", "type": "full time"},
    {"salary": "4000", "title": "Analista de Software", "type": "full time"},
    {"salary": "1400", "title": "Auxiliar usinagem", "type": " full time"},
    {"salary": "5000", "title": "Gerente comercial", "type": " full time"},
]

min = [
    {"salary": "1400", "title": "Auxiliar usinagem", "type": " full time"},
    {"salary": "2000", "title": "Maquinista", "type": "trainee"},
    {"salary": "3000", "title": "Motorista", "type": "full time"},
    {"salary": "4000", "title": "Analista de Software", "type": "full time"},
    {"salary": "5000", "title": "Gerente comercial", "type": " full time"},
]


def test_sort_by_criteria():
    assert min == sort_by(jobs_list, 'min_salary')

from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    archive = read(path)
    max_salary = 0
    for item in archive:
        if 'invalid' != item['max_salary'] != '':
            value = int(item['max_salary'])
            if value > max_salary:
                max_salary = value
    return max_salary


def get_min_salary(path: str) -> int:
    archive = read(path)
    min_salary = get_max_salary(path)
    for item in archive:
        if 'invalid' != item['min_salary'] != '':
            value = int(item['min_salary'])
            if value < min_salary:
                min_salary = value
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    min, max = 0, 0
    try:
        min = int(job['min_salary'])
        max = int(job['max_salary'])
    except (TypeError, KeyError):
        raise ValueError

    if min > max or type(salary) not in [int, str]:
        raise ValueError
    return min <= (salary if type(salary) == int else int(salary)) <= max


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

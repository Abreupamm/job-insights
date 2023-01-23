from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        archive = csv.DictReader(file, delimiter=',', quotechar='"')
        return list(archive)


def get_unique_job_types(path: str) -> List[str]:
    archive = read(path)
    unique_list = list()
    for item in archive:
        if item is not None:
            unique_item = item['job_type']
            unique_list.append(unique_item)
    return list(set(unique_list))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

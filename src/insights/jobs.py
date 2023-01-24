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
        if item['job_type'] != '':
            unique_item = item['job_type']
            unique_list.append(unique_item)
    return list(set(unique_list))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    new_jobs_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            new_jobs_list.append(job)

    return new_jobs_list

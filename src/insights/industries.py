from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    archive = read(path)
    unique_list = list()
    for item in archive:
        if item['industry'] != '':
            unique_item = item['industry']
            unique_list.append(unique_item)
    return list(set(unique_list))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    new_industry_list = []
    for job in jobs:
        if job['industry'] == industry:
            new_industry_list.append(job)
        
    return new_industry_list

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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

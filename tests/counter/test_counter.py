from src.pre_built.counter import count_ocurrences


def test_counter():
    ocurrences = count_ocurrences('data/jobs.csv', 'stack')
    assert ocurrences == 211

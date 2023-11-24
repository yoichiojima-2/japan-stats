import re


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


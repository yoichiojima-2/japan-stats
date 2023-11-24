import re


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


def strip_prefix(metrix_title):
    return re.sub(r"\w\d*_", "", metrix_title)

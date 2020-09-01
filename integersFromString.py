import re

def integersFromString(s):
    return int(re.search(r'\d+', s))
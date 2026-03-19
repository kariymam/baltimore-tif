import re

def location(name):
    location = re.sub(r"\s+", "+", f"{name}")
    return location


def test_single_space():
    assert location('Carrolton Ridge') == 'Carrolton+Ridge'

def test_multi_space():
    assert location('East Baltimore Midway') == 'East+Baltimore+Midway'


def query_out_fields(list):
    return ",".join(list)

def test_query_out_fields():
    assert query_out_fields(['FULLADDR', 'BLOCKLOT', 'Ownership', 'Orig_Criteria', 'Current_Criteria', 'VRPA']) == 'FULLADDR,BLOCKLOT,Ownership,Orig_Criteria,Current_Criteria,VRPA'

# Loop through neighborhoods in BVRI csv and count the appearance of each neighborhood


#FULLADDR%2C+BLOCKLOT%2C+Ownership%2C+Orig_Criteria%2C+Current_Criteria%2C+VRPA
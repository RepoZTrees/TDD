import tables

def test_tab():
    actual_result = tables.tab(3,10)
    expected_result = [3,6,9,12,15,18,21,24,27,30]
    assert actual_result == expected_result

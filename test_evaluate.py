import evaluate

def test_evaluate():
    actual_value = evaluate.evaluate("34*62+12-3/")
    expected_value = [12,8,3]
    assert actual_value == expected_value

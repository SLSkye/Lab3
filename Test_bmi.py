import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.67,54)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75,77)
    assert (result ==1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.68,40)
    assert (result == -1)
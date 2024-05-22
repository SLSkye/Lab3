import employee_info


def test_get_employees_by_age_range():
    sample_lower_age = 10
    sample_upper_age = 33
    test_employeess = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}, 
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000} ]

    result = employee_info.get_employees_by_age_range(sample_lower_age, sample_upper_age)
    assert (result == test_employeess)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    sample_dept = "Marketing"
    test_employeess = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000} ]

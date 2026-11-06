
from main import calculate_result


def test_total_and_average():
    total, average, grade = calculate_result([90, 85, 95, 80, 90])

    assert total == 440
    assert average == 88
    assert grade == "A"


def test_grade_a_plus():
    _, _, grade = calculate_result([95, 92, 94, 96, 93])

    assert grade == "A+"


def test_grade_a():
    _, _, grade = calculate_result([80, 85, 82, 84, 89])

    assert grade == "A"


def test_grade_b():
    _, _, grade = calculate_result([70, 75, 72, 74, 79])

    assert grade == "B"


def test_grade_c():
    _, _, grade = calculate_result([60, 65, 62, 64, 69])

    assert grade == "C"


def test_grade_d():
    _, _, grade = calculate_result([40, 45, 50, 55, 59])

    assert grade == "D"


def test_fail():
    _, _, grade = calculate_result([90, 85, 80, 30, 95])

    assert grade == "Fail"

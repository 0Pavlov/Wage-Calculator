from functions import calculate


def test_day_shifts():
    """Tests calculate function with various day shifts and day hour rates."""
    assert calculate(day_shifts=1, day_hour=275, bonus_speed=False) == 275 * 8
    assert calculate(day_shifts=1, day_hour=300, bonus_speed=False) == 300 * 8
    assert calculate(day_shifts=3, day_hour=100, bonus_speed=False) == 100 * 8 * 3


def test_night_shifts():
    """Tests calculate function with various night shifts and day hour rates."""
    assert calculate(night_shifts=1, day_hour=250, bonus_speed=False) == 3150
    valid_result = ((350 + (350 * 0.2)) * 8 * 3) + 350 * 3 * 3
    assert calculate(night_shifts=3, day_hour=350, bonus_speed=False) == valid_result


def test_no_arguments_except_bonuses():
    """Tests bonuses calculation."""
    assert calculate(bonus_speed=True, bonus_performance=True) == 7000
    assert calculate(bonus_speed=True, bonus_performance=False) == 3500
    assert calculate(bonus_speed=False, bonus_performance=True) == 3500


def test_no_shifts_no_bonuses():
    """Tests calculate function returns zero, when no shifts or hours passed."""
    assert calculate(bonus_speed=False, bonus_performance=False) == 0


def test_type():
    """Tests the return type."""
    assert type(calculate()) == float
    assert type(calculate(day_shifts=10)) == float
    assert type(calculate(night_shifts=3)) == float
    assert type(calculate(bonus_speed=True, bonus_performance=True)) == float
    assert type(calculate(night_hours=-35)) == float


def test_hours_negative():
    """Tests additional hours are subtracted if negative."""
    assert calculate(bonus_speed=False, day_hour=200, day_hours=-1) == -200
    assert calculate(bonus_speed=False, day_hour=1, night_hours=-1) == -(1 + (1 * 0.2))


def test_hours_positive():
    """Tests additional hours being positive."""
    assert calculate(bonus_speed=False, day_hour=200, day_hours=1) == 200
    assert calculate(bonus_speed=False, day_hour=1, night_hours=1) == 1 + (1 * 0.2)


def test_edge_cases():
    """Tests calculate function with edge case values."""
    assert calculate(bonus_speed=False, day_hour=0, day_hours=20, night_shifts=10) == 0
    assert calculate(bonus_speed=False, day_shifts=1000000, day_hour=1000) == 8000000000

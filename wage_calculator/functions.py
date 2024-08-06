def calculate(night_shifts: int = 0,
              day_shifts: int = 0,
              day_hour: int = 275,
              bonus_speed: bool = True,
              bonus_performance: bool = False,
              day_hours: float = 0,
              night_hours: float = 0,
              ) -> float:
    """Calculates the total earnings of a worker.

    This function takes into account day and night shifts, hourly rates, bonuses,
    and additional hours to calculate the total earnings.

    Args:
        night_shifts (int, optional): Number of full night shifts worked. Defaults to 0.
        day_shifts (int, optional): Number of full day shifts worked. Defaults to 0.
        day_hour (int, optional): Hourly rate for day shifts. Night hourly rate is
        calculated from it. Defaults to 275.
        bonus_speed (bool, optional): Indicates if a speed bonus is earned.
        Defaults to True.
        bonus_performance (bool, optional): Indicates if a performance bonus is earned.
        Defaults to False.
        day_hours (float, optional): Additional day hours worked (outside full shifts).
        Defaults to 0.
        night_hours (float, optional): Additional night hours worked
        (outside full shifts). Defaults to 0.

    Returns:
        float: The total amount earned.
    """
    # Night hourly rate
    night_hour: float = day_hour + day_hour * 0.2

    # Amount of hours:
    # Night
    day_hours_per_night = 3
    night_hours_per_night = 8
    total_night_hours = night_shifts * night_hours_per_night + night_hours

    # Day
    day_hours_per_day = 8
    total_day_hours = ((night_shifts * day_hours_per_night) +
                       (day_shifts * day_hours_per_day) +
                       day_hours)

    # Bonus calculation
    bonus = 0
    if bonus_speed:
        bonus += 3500
    if bonus_performance:
        bonus += 3500

    # Convert to money
    total_day_hours_cost = total_day_hours * day_hour
    total_night_hours_cost = total_night_hours * night_hour

    # Total earned
    total_earned = total_day_hours_cost + total_night_hours_cost + bonus
    return total_earned

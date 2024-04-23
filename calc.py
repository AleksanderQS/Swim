def calculate_average_speed(time_entries, distance_entries):
    try:
        total_time = sum(float(time_entry.get()) for time_entry in time_entries)
        total_distance = sum(float(distance_entry.get()) for distance_entry in distance_entries)
        average_speed = total_distance / total_time
        time_100m = 100 / average_speed
        return average_speed, time_100m
    except ValueError:
        return None, None


def estimate_time_100m(average_speed):
    if average_speed:
        return 100 / average_speed
    else:
        return None

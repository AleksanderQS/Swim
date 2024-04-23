from ui import SwimmingProgressTracker
from calc import calculate_average_speed
from data_manager import save_data


def main():
    app = SwimmingProgressTracker(lambda: calculate_callback(app))
    app.run()


def calculate_callback(app):
    average_speed, time_100m = calculate_average_speed(app.time_entries, app.distance_entries)
    if average_speed is not None:
        app.speed_label.config(text=f"Your average speed is: {average_speed:.2f} m/s")
        app.time_100m_label.config(text=f"Your estimated time for 100 meters is: {time_100m:.2f} seconds")
        save_data(app.time_entries, app.distance_entries)  # Salvar os dados
    else:
        app.speed_label.config(text="Please enter valid numeric values for time and distance.")


if __name__ == "__main__":
    main()

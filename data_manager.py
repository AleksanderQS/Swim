import csv
import glob
from datetime import datetime


def save_data(time_entries, distance_entries):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"data_{current_date}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time (seconds)", "Distance (meters)", "Average Speed (m/s)"])
        for time_entry, distance_entry in zip(time_entries, distance_entries):
            time = float(time_entry.get())
            distance = float(distance_entry.get())
            average_speed = distance / time
            writer.writerow([time, distance, average_speed])

    print(f"Dados salvos em {filename}")


def load_data():
    data = []
    for filename in glob.glob("data_*.csv"):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Pular cabeçalho
            times = []
            for row in reader:
                time = float(row[0])
                distance = float(row[1])
                average_speed = distance / time
                times.append(average_speed)
            if times:  # Verificar se a lista de tempos não está vazia
                average_speed = sum(times) / len(times)
                average_time_for_100m = 100 / average_speed
                data.append((filename[5:-4], average_speed, average_time_for_100m))
    return data

import tkinter as tk
import matplotlib.pyplot as plt
from data_manager import load_data


class SwimmingProgressTracker:
    def __init__(self, calculate_callback):
        self.root = tk.Tk()
        self.root.title("Swimming Progress Tracker")

        self.num_entries_var = tk.StringVar()
        self.num_entries_entry = tk.Entry(self.root, textvariable=self.num_entries_var)
        self.num_entries_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add today laps", command=self.add_entries)
        self.add_button.pack(pady=5)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.speed_label = tk.Label(self.root, text="")
        self.speed_label.pack(pady=5)

        self.time_100m_label = tk.Label(self.root, text="")
        self.time_100m_label.pack(pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=calculate_callback)
        self.calculate_button.pack(pady=10)

        self.time_entries = []  # Initialize time_entries list
        self.distance_entries = []  # Initialize distance_entries list

        self.plot_button = tk.Button(self.root, text="Plot Data", command=self.plot_data)
        self.plot_button.pack(pady=5)

    def add_entries(self):
        num_entries = int(self.num_entries_var.get())

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.time_entries.clear()  # Clear time_entries list
        self.distance_entries.clear()  # Clear distance_entries list

        for i in range(num_entries):
            tk.Label(self.frame, text=f"Entry {i+1}:").grid(row=i, column=0, padx=5, pady=5)
            time_label = tk.Label(self.frame, text="Time (seconds):")
            time_label.grid(row=i, column=1, padx=5, pady=5)
            time_entry = tk.Entry(self.frame)
            time_entry.grid(row=i, column=2, padx=5, pady=5)
            distance_label = tk.Label(self.frame, text="Distance (meters):")
            distance_label.grid(row=i, column=3, padx=5, pady=5)
            distance_entry = tk.Entry(self.frame)
            distance_entry.grid(row=i, column=4, padx=5, pady=5)
            self.time_entries.append(time_entry)
            self.distance_entries.append(distance_entry)

    @staticmethod
    def plot_data():
        data = load_data()

        dates = [entry[0] for entry in data]
        average_speeds = [entry[2] for entry in data]

        # Multiplicar a velocidade média pela distância desejada (100 metros)
        times_for_100m = [100 / speed for speed in average_speeds]

        plt.plot(dates, times_for_100m, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Time for 100m (seconds)')
        plt.title('Time for 100m over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run(self):
        self.root.mainloop()

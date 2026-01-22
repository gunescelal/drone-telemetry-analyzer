import csv


def load_data(file_path):
    """
    Loads telemetry data from a CSV file and returns a list of records.
    """
    data = []

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "time": int(row["time"]),
                "altitude": int(row["altitude"]),
                "speed": int(row["speed"]),
                "battery": int(row["battery"]),
                "temperature": int(row["temperature"])
            })

    return data


def analyze_data(data):
    """
    Analyzes telemetry data and returns basic statistics.
    """
    max_altitude = max(d["altitude"] for d in data)
    avg_speed = sum(d["speed"] for d in data) / len(data)
    min_battery = min(d["battery"] for d in data)
    max_temperature = max(d["temperature"] for d in data)

    analysis = {
        "max_altitude": max_altitude,
        "average_speed": round(avg_speed, 2),
        "min_battery": min_battery,
        "max_temperature": max_temperature
    }

    return analysis
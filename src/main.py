from analyzer import load_data, analyze_data
from alerts import check_alerts


def main():
    print("=== Drone Telemetry Analyzer ===")

    # Load telemetry data
    data = load_data("../data/telemetry.csv")

    # Analyze data
    analysis = analyze_data(data)

    print("\n--- Flight Analysis ---")
    for key, value in analysis.items():
        print(f"{key}: {value}")

    # Check alerts
    alerts = check_alerts(data)

    if alerts:
        print("\n--- Alerts ---")
        for alert in alerts:
            print(alert)
    else:
        print("\nNo alerts detected.")


if __name__ == "__main__":
    main()
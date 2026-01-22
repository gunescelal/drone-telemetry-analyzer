def check_alerts(data):
    """
    Checks telemetry data for critical conditions.
    Returns a list of alert messages.
    """
    alerts = []

    for record in data:
        if record["battery"] < 80:
            alerts.append(
                f"Low battery detected at time {record['time']}s: {record['battery']}%"
            )

        if record["temperature"] > 45:
            alerts.append(
                f" High temperature detected at time {record['time']}s: {record['temperature']}°C"
            )

    return alerts
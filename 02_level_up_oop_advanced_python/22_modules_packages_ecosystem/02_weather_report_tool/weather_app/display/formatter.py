from datetime import datetime

def format_report(data, city):
    """
    Extract weather information and format it
    into a readable report.
    This belongs in display because formatting
    and presenting data is separate from fetching it.
    """
    current = data["current_condition"][0]
    temperature = current["temp_C"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]
    description = current["weatherDesc"][0]["value"]
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    report = f"""
Weather Report for {city}
Generated: {timestamp}
Temperature: {temperature}°C
Humidity: {humidity}%
Wind: {wind_speed} km/h
Conditions: {description}
"""
    return report.strip()
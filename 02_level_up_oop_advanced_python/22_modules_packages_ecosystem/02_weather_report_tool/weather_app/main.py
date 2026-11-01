# Import weather fetching & formatting function.
from api.fetcher import fetch_weather
from display.formatter import format_report

def main():
    try:
        city=input("Enter city:").strip()
        if not city:
            print("Error: Please enter valid a city name.")
            return
        data=fetch_weather(city)
        report=format_report(data,city)
        print(report)
    except ConnectionError as error:
        print(f"Error: {error}")
    except TimeoutError as error:
        print(f"Error: {error}")    
    except ValueError as error:
        print(f"Error: {error}")    
    except (KeyError,IndexError,TypeError):
        print("Error: Weather data received was incomplete.")                
    except KeyboardInterrupt:
        print("Weather report cancelled.")    
    except Exception:
        print("Error: Something unexcepted went wrong.")    
# Run the application only when main.py is executed directly.
if __name__ == "__main__":
    main()
        
"""Weather Report Tool
Third-party packages, virtual environments, and project organization
Build a weather report tool using the requests library.

Setup first:
1. Create a virtual environment
2. Install requests: pip install requests
3. Create requirements.txt

Project structure:

weather_app/
├── api/
│   ├── __init__.py
│   └── fetcher.py         — fetch_weather(city) function
├── display/
│   ├── __init__.py
│   └── formatter.py       — format_report(data) function
├── main.py
├── requirements.txt
└── venv/                   — NOT committed

fetcher.py:
- fetch_weather(city) — calls requests.get(f"https://wttr.in/{city}?format=j1")
- Returns parsed JSON data
- Handles: network errors (requests.ConnectionError), invalid city (check response status), timeouts

formatter.py:
- format_report(data, city) — extracts temperature, humidity, wind speed, weather description from the JSON
- Returns a formatted multi-line string with timestamp (use datetime)

main.py:
- Asks user for a city
- Fetches and displays the weather report
- Handles all errors gracefully — never crashes

Example output:

Enter city: Pune

Weather Report for Pune
Generated: 2024-01-15 14:30:00
Temperature: 28°C
Humidity: 65%
Wind: 12 km/h
Conditions: Partly Cloudy

Enter city: asdfghjkl
Error: Could not find weather data for "asdfghjkl"
"""
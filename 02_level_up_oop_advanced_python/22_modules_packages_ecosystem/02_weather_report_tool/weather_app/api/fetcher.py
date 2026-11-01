import requests

def fetch_weather(city):
    """
    Fetch weather information for a given city.

    This function belongs in the api package because
    its responsibility is communicating with the API.
    """

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if (
            not isinstance(data, dict)
            or not data.get("current_condition")
        ):
            raise ValueError(
                f'Could not find weather data for "{city}"'
            )
        return data
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "Unable to connect. Please check your internet connection."
        )
    except requests.exceptions.Timeout:
        raise TimeoutError(
            "The weather service took too long to respond."
        )
    except requests.exceptions.HTTPError:
        raise ValueError(
            f'Could not find weather data for "{city}"'
        )
    except (ValueError, requests.exceptions.JSONDecodeError):
        raise ValueError(
            f'Could not find weather data for "{city}"'
        )
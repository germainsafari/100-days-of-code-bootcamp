import requests
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key ="11b4f9408e3dcc2b8f4076404741677e"
weather_params = {
    "lat": 52.406376,
    "lon": 16.925167,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

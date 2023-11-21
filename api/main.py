from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/get_weather")
async def get_weather():
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/istanbul?unitGroup=metric&key=NHF74VS7S9SWWZ46MY47A555E&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        return {
            "istanbul": response.json()["currentConditions"]["feelslike"]
        }
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}


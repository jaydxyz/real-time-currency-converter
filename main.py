from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/convert")
def convert_currency(amount: float, from_currency: str, to_currency: str):
    # Make an API call to fetch the latest exchange rates
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()
    
    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]
    
    # Calculate the converted amount
    converted_amount = amount * exchange_rate
    
    # Return the converted amount as a JSON response
    return {"converted_amount": converted_amount}
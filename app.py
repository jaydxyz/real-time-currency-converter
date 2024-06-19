from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # Make a request to the FastAPI backend
    response = requests.get(f"http://localhost:8000/convert?amount={amount}&from_currency={from_currency}&to_currency={to_currency}")
    data = response.json()

    converted_amount = data['converted_amount']
    return render_template('result.html', amount=amount, from_currency=from_currency, to_currency=to_currency, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
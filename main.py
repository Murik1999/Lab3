from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', base_currency=None, target_currency=None, amount=None, converted_amount=None)

@app.route('/convert', methods=['POST'])
def convert():
    api_key = '2d554fd01c2f43f6a62a7994ca76dc7a'
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    response = requests.get(url)
    data = response.json()
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']
    amount = float(request.form['amount'])
    exchange_rate = data['rates'][target_currency]
    converted_amount = amount * exchange_rate

    return render_template('index.html', base_currency=base_currency, target_currency=target_currency, amount=amount, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run()
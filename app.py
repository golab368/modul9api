import requests
from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/')
def convert():

    response = requests.get(
        "http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    return render_template('index.html',  values=data[0]["rates"])


@app.route("/", methods=["POST"])
def value():

    currency_and_values_of_them = request.form["selected"]
    how_much_U_wanna_exchange = request.form["how_much_U_wanna_exchange"]

    x = [s for s in currency_and_values_of_them if s.isdigit()]
    result = int(''.join(str(i) for i in x))
    l = list(str(result))
    l.insert(1, '.')
    amount_of_selected_currency = "".join(l)

    currency_and_values_of_them1 = request.form["selected1"]
    x1 = [s for s in currency_and_values_of_them1 if s.isdigit()]
    result1 = int(''.join(str(i) for i in x1))
    l1 = list(str(result1))
    l1.insert(1, '.')
    amount_of_selected_currency1 = "".join(l1)

    result_of_exchange = (float(how_much_U_wanna_exchange) * float(
        amount_of_selected_currency) * float(amount_of_selected_currency1))

    return render_template("index.html", currency_and_values_of_them=currency_and_values_of_them, how_much_U_wanna_exchange=how_much_U_wanna_exchange, amount_of_selected_currency=amount_of_selected_currency, currency_and_values_of_them1=currency_and_values_of_them1, result_of_exchange=result_of_exchange)

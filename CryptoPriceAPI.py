from flask import Flask, jsonify
import ccxt

app = Flask(__name__)

@app.route('/api/criptomoedas/<symbol>')
def get_price(symbol):
    exchanges = ['binance', 'bitfinex', 'bittrex', 'coinbasepro', 'kraken']
    result = {}
    for exchange_id in exchanges:
        exchange = getattr(ccxt, exchange_id)()
        ticker = exchange.fetch_ticker(symbol)
        result[exchange_id] = {
            'bid': ticker['bid'],
            'ask': ticker['ask'],
            'last': ticker['last'],
        }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

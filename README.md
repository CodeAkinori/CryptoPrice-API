# CryptoPrice API
CryptoPrice is a RESTful API that provides real-time price information for various cryptocurrencies. It uses the CCXT library to fetch prices from popular cryptocurrency exchanges such as Binance, Bitfinex, Bittrex, Coinbase Pro, and Kraken.

## Usage
To use the API, simply send a GET request to the following endpoint:
```
https://example.com/api/criptomoedas/<symbol>
```

Replace <symbol> with the symbol of the cryptocurrency you want to get price information for (e.g. BTC, ETH, LTC, etc.).

The API will return a JSON object with the current bid, ask, and last prices for the specified cryptocurrency on each exchange. The JSON object will be in the following format:
```
{
    "binance": {
        "bid": 48000.0,
        "ask": 48001.0,
        "last": 48000.5
    },
    "bitfinex": {
        "bid": 47998.0,
        "ask": 48000.0,
        "last": 47999.5
    },
    "bittrex": {
        "bid": 47950.0,
        "ask": 48050.0,
        "last": 48000.0
    },
    "coinbasepro": {
        "bid": 48001.0,
        "ask": 48002.0,
        "last": 48001.5
    },
    "kraken": {
        "bid": 48005.0,
        "ask": 48010.0,
        "last": 48007.5
    }
}
```

## Rate Limit
The API has a rate limit of 10 requests per minute per IP address. If you exceed this limit, you will receive a 429 error response.

## Disclaimer
The price information provided by this API is for informational purposes only and should not be relied upon for investment decisions. Prices may be delayed and may not reflect the current market price of the cryptocurrency. Always do your own research and make your own investment decisions.
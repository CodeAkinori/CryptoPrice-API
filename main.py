# main.py
import ccxt  # sync version
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Crypto Price API", version="1.0")

# Supported exchanges
EXCHANGES = ['binance', 'bitfinex', 'coinbase', 'kraken']

@app.get("/api/criptomoedas/{base}/{quote}")
def get_price(base: str, quote: str):
    """
    Retorna o preço de uma criptomoeda em múltiplas exchanges.
    
    - base: moeda base, ex: BTC
    - quote: moeda de cotação, ex: USDT
    """
    symbol = f"{base}/{quote}".upper()  # Cria o símbolo no formato CCXT
    result = {}

    for exchange_id in EXCHANGES:
        try:
            exchange_class = getattr(ccxt, exchange_id)
            exchange = exchange_class()
            ticker = exchange.fetch_ticker(symbol)
            result[exchange_id] = {
                "bid": ticker.get("bid"),
                "ask": ticker.get("ask"),
                "last": ticker.get("last"),
            }
        except ccxt.BaseError as e:
            # Retorna erro por exchange se o símbolo não existir ou outro erro
            result[exchange_id] = {"error": str(e)}

    return JSONResponse(content=result)

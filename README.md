# Crypto Price API

A FastAPI service that fetches cryptocurrency prices from multiple exchanges using CCXT.

---

## Requirements

- Python ≥ 3.8
- Install dependencies:

pip install fastapi uvicorn ccxt

---

## Running the API

uvicorn main:app --reload

* Server: http://127.0.0.1:8000
* Interactive docs: http://127.0.0.1:8000/docs
* Redoc docs: http://127.0.0.1:8000/redoc

---

## Routes

### GET /api/criptomoedas/{base}/{quote}

Fetches bid, ask, and last prices for a cryptocurrency pair across multiple exchanges.

* **Path Parameters**

  * `base` – base currency, e.g., `BTC`
  * `quote` – quote currency, e.g., `USDT`

* **Example Request**

```
GET /api/criptomoedas/BTC/USDT
```

* **Example Response**

```json
{
  "binance": {"bid": 27650.0, "ask": 27651.0, "last": 27650.5},
  "bitfinex": {"bid": 27648.5, "ask": 27650.0, "last": 27649.2},
  "coinbasepro": {"bid": 27651.0, "ask": 27653.0, "last": 27652.1},
  "kraken": {"bid": 27649.5, "ask": 27651.5, "last": 27650.8}
}
```

* **Error Handling**

If a symbol is not supported on an exchange:

```json
{
  "bitfinex": {"error": "Symbol not found"}
}
```

---

## Example Usage

### Using curl

```bash
curl http://127.0.0.1:8000/api/criptomoedas/BTC/USDT
```

### Using Python requests

```python
import requests

base = "BTC"
quote = "USDT"
response = requests.get(f"http://127.0.0.1:8000/api/criptomoedas/{base}/{quote}")
data = response.json()
print(data)
```

---

## Notes

* Only exchanges listed in the `EXCHANGES` array are queried.
* Some exchanges may not support certain symbols, and an error will be returned for them.
* Use the `/docs` route to interact with the API via Swagger UI.

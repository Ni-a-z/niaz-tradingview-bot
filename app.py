from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

@app.route("/")
def home():
    return "Niaz Trade Bot Online"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    signal = data.get("signal", "UNKNOWN")
    symbol = data.get("symbol", "UNKNOWN")
    price = data.get("price", "UNKNOWN")

    msg = f"""
🔥 NIAZ SIGNAL

Signal: {signal}
Pair: {symbol}
Price: {price}
"""

    send(msg)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

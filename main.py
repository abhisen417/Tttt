
import json
from flask import Flask, request
import requests
import datetime
import os

app = Flask(__name__)

# Telegram config
TELEGRAM_BOT_TOKEN = "8001032388:AAE-2k-ixahbRNITX_0sOxId_PLKDJyFNJU"
TELEGRAM_CHAT_ID = "7606414310"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("ticker", "Unknown")
    side = data.get("side", "BUY/SELL")
    price = data.get("price", "N/A")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"🟢 Paper Trade Alert (Webhook)

📈 Symbol: {symbol}
📊 Side: {side}
💵 Price: {price}
🕒 Time: {time}"
    send_telegram_message(message)
    return {"status": "Message sent to Telegram ✅"}, 200

# Required to run on Render.com
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

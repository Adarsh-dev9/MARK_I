import logging
import json
import os
import requests
from flask import Flask, render_template, request

# Setup basic logging (without Azure)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Flask App
app = Flask(__name__)

# Function to get current time from public API
def query_message():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en", timeout=5)
        if response.status_code == 200:
            message = json.loads(response.text)['text']
            logger.info('Successfully queried public API')
            return message
        else:
            logger.error(f"Error querying API. Status code: {response.status_code}")
            return "Unavailable"
    except Exception:
        logger.error('Failed to contact public API', exc_info=True)
        return "Unavailable"

# Replace Azure Key Vault Secret with a default word
def get_secret():
    return "Fallback Word of the Day"

# Get user IP Address
def get_ip(web_request):
    return web_request.remote_addr

# Render the webpage
@app.route("/")
def index():
    ipinfo = get_ip(web_request=request)
    wordoftheday = get_secret()  # No Azure Key Vault required
    message = query_message()
    return render_template('index.html', wordoftheday=wordoftheday, message=message, ip=ipinfo)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
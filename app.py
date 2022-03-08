import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "white": "#ffffff",
    "black": "#0000000"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    date = str(datetime.now()).split()[0]
    return ""


if __name__ == "__main__":
    app.run()

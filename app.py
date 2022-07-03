import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    date = str(datetime.now()).split()[0]
    return render_template('index.html', date=date)


if __name__ == "__main__":
    app.run()

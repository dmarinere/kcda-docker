import os
from flask import Flask, render_template
from datetime import datetime 
app = Flask(__name__)

@app.route("/")
def main():
    date = str(datetime.now()).split()[0]
    print(date)
    return render_template('index.html')
                            


if __name__ == "__main__":
    app.run()

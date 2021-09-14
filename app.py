from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/financial")
def financial():
    return render_template('financial.html')

@app.route("/future")
def future():
    return render_template('future.html')

@app.route("/customer")
def customer():
    return render_template('customer.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')


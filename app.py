from flask import Flask, render_template, request
from utils.gemini_helper import get_ai_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/advice", methods=["POST"])
def advice():
    income = request.form["income"]
    expenses = request.form["expenses"]
    goal = request.form["goal"]
    product_price = request.form["product_price"]
    months = request.form["months"]
    

    result = get_ai_response(income, expenses, goal, product_price, months)

    return render_template("advice.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
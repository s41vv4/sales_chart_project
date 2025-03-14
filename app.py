from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        date = request.form["date"]
        name = request.form["name"]
        daily_sales = float(request.form["sales"])

        # Performance evaluation
        if daily_sales >= 400:
            result = f"{name} - Very Good"
        elif 350 <= daily_sales < 400:
            result = f"{name} - Good"
        elif 300 <= daily_sales < 350:
            result = f"{name} - Bad"
        else:
            result = f"{name} - Very Bad"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

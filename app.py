from flask import Flask, jsonify, render_template, request, redirect, url_for
from simulation import run_monte_carlo
from plotting import plot_simulation
from summary_clean import get_summary

app = Flask(__name__)
chart_html_content = ""
summary_result = ""
success_result = 0.0

@app.route("/", methods=["GET", "POST"])
def home():
    global chart_html_content, summary_result, success_result
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            retirement_age = int(request.form["retirement_age"])
            savings = float(request.form["savings"])
            income = float(request.form["income"])
            monthly_expense = float(request.form["monthly_expense"])

            df, success = run_monte_carlo(age, retirement_age, savings, income, monthly_expense)
            chart_html_content = plot_simulation(df)
            summary_result = get_summary(success, age, retirement_age)
            success_result = round(success, 2)

            return redirect(url_for("result"))

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    df, success = run_monte_carlo(
        data["age"], data["retirement_age"],
        data["savings"], data["income"],
        data["monthly_expense"]
    )
    chart_html = plot_simulation(df)
    summary = get_summary(success, data["age"], data["retirement_age"])
    
    return jsonify({
        "chart": chart_html,
        "success_rate": success,
        "summary": summary
    })

@app.route("/result")
def result():
    global chart_html_content, summary_result, success_result
    return render_template("result.html",
                           chart=chart_html_content,
                           summary=summary_result,
                           success_rate=success_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

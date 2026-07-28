from flask import Flask, render_template, request

app = Flask(__name__)

sales = []

@app.route("/", methods=["GET", "POST"])
def index():
    error_msg = None

    if request.method == "POST":
        action = request.form.get("action")

        # Clear button
        if action == "clear":
            sales.clear()

        # Add record
        elif action == "add":
            date = request.form.get("date")
            amount_input = request.form.get("amount")

            try:
                amount = float(amount_input)

                if amount <= 0:
                    error_msg = "Sales amount must be greater than 0."
                else:
                    sales.append({
                        "date": date,
                        "amount": amount
                    })

            except ValueError:
                error_msg = "Please enter a valid amount."

    metrics = None

    if sales:
        amounts = [sale["amount"] for sale in sales]

        total_sales = sum(amounts)
        avg_sales = total_sales / len(amounts)

        best_sale = max(amounts)
        worst_sale = min(amounts)

        best_record = next(
            sale for sale in sales
            if sale["amount"] == best_sale
        )

        worst_record = next(
            sale for sale in sales
            if sale["amount"] == worst_sale
        )

        metrics = {
            "total": total_sales,
            "avg": avg_sales,
            "best_amount": best_sale,
            "best_date": best_record["date"],
            "worst_amount": worst_sale,
            "worst_date": worst_record["date"]
        }

    return render_template(
        "index.html",
        sales=sales,
        metrics=metrics,
        error_msg=error_msg
    )

if __name__ == "__main__":
    app.run(debug=True)
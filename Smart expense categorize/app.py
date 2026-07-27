from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        description = request.form["description"].strip()
        amount_input = request.form["amount"]

        # Validating description
        if not any(char.isalpha() for char in description):
            error = "Please enter a valid item name (must contain letters)."
            return render_template("index.html", error=error)

        # Validating amount
        try:
            amount = float(amount_input)

            if amount < 0:
                error = "Amount cannot be negative."
                return render_template("index.html", error=error)

        except ValueError:
            error = "Please enter a valid amount."
            return render_template("index.html", error=error)

        description_lower = description.lower()

        category = "Other"

        if any(word in description_lower for word in ["food", "grocery", "restaurant"]):
            category = "Food & Dining"

        elif any(word in description_lower for word in ["rent", "house", "apartment"]):
            category = "Housing"

        elif any(word in description_lower for word in ["gas", "bus", "ride share"]):
            category = "Transportation"

        elif any(word in description_lower for word in ["movie", "game", "netflix"]):
            category = "Entertainment"

        elif any(word in description_lower for word in ["doctor", "pharmacy"]):
            category = "Healthcare"

        if amount > 100:
            advice = "Large expense. Review your spending."
        elif amount > 50:
            advice = "Moderate expense."
        else:
            advice = "Small expense. Keep it low."

        result = {
            "description": description.title(),
            "amount": amount,
            "category": category,
            "advice": advice
        }

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
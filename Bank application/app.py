from flask import Flask, render_template, request
from Bankclass import Bank

app = Flask(__name__)

accounts = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu", methods=["POST"])
def menu():

    choice = request.form.get("choice")

    if choice == "1":
        return render_template("create.html")

    elif choice == "2":
        return render_template("deposit.html")

    elif choice == "3":
        return render_template("withdrawl.html")

    elif choice == "4":
        return render_template("details.html")

    elif choice == "5":
        return render_template(
            "message.html",
            message="Thank you for trusting us."
        )

    return render_template(
        "message.html",
        message="Invalid Choice"
    )


@app.route("/create", methods=["POST"])
def create():

    name = request.form["name"]
    balance = int(request.form["balance"])

    account = Bank(name, balance)

    accounts.append(account)

    return render_template(
        "message.html",
        message=f"""
Account Created Successfully

Account Name : {account.account_name}
Account Number : {account.account_number}
Balance : Rs. {account.initial_balance}
"""
    )


@app.route("/deposit", methods=["POST"])
def deposit():

    acc_number = request.form["acc_number"]
    amount = int(request.form["amount"])

    for account in accounts:

        if account.account_number == acc_number:

            account.deposit(amount)

            return render_template(
                "message.html",
                message=f"""
                Deposit Successful
                Current Balance : Rs. {account.initial_balance}
                """
            )

    return render_template(
        "message.html",
        message="Account Not Found"
    )


@app.route("/withdraw", methods=["POST"])
def withdraw():

    acc_number = request.form["acc_number"]
    amount = int(request.form["amount"])

    for account in accounts:

        if account.account_number == acc_number:

            account.withdrawl(amount)

            return render_template(
                "message.html",
                message=f"""
                Withdrawal Successful
                Current Balance : Rs. {account.initial_balance}
                """
            )

    return render_template(
        "message.html",
        message="Account Not Found"
    )


@app.route("/details", methods=["POST"])
def details():

    acc_number = request.form["acc_number"]

    for account in accounts:

        if account.account_number == acc_number:

            return render_template(
                "message.html",
                message=f"""
                Account Name : {account.account_name}
                Account Number : {account.account_number}
                Balance : Rs. {account.initial_balance}
                """
            )

    return render_template(
        "message.html",
        message="Account Not Found"
    )


if __name__ == "__main__":
    app.run(debug=True)
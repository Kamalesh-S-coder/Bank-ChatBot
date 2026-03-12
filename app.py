from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.secret_key = "banksecret123"


# DATABASE CONNECTION
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="bankdb",
        user="postgres",
        password="postgres"   # change if your postgres password is different
    )
    return conn


# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            session["user"] = username
            session["chat_history"] = []
            return redirect("/chatbot")

        else:
            return render_template("login.html", error="Invalid Username or Password")

    return render_template("login.html")


# CHATBOT LOGIC
def get_bot_response(msg):

    msg = msg.lower()

    if "balance" in msg:
        return "Your current balance is ₹25,000"

    elif "loan" in msg:
        return "We offer Home Loan, Car Loan and Personal Loan."

    elif "credit card" in msg:
        return "Your credit card limit is ₹1,00,000"

    elif "hello" in msg or "hi" in msg:
        return "Hello! How can I help you today?"

    else:
        return "Sorry I didn't understand that. Try asking about balance, loans or credit cards."


# CHATBOT PAGE
@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    if "user" not in session:
        return redirect("/")

    if request.method == "POST":

        user_msg = request.form["message"]

        bot_reply = get_bot_response(user_msg)

        session["chat_history"].append(("You", user_msg))
        session["chat_history"].append(("Bot", bot_reply))

    return render_template(
        "chatbot.html",
        username=session["user"],
        chat_history=session["chat_history"]
    )


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
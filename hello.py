from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def save_data(data):
    with open("database.csv", mode='a', newline="") as database:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        data_csv = csv.writer(database,  delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_csv.writerow([email, subject, message])

@app.route("/contact_me", methods=["POST", "GET"])
def contact_me():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            save_data(data)
            return redirect("thank.html")
        except:
            return "Data did not save in the server!!"

    else:
        return "Something is wrong!!"


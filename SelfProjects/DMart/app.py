from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def enter():
    return render_template("index.html", tot = 0, disc = 0, final = 0)


@app.route("/cal", methods=["POST"])
def calculate():
    if (request.method == "POST"):
        items = request.form.getlist("selectedItems")
        totalAmount = 0
        discount = 0
        finalAmount = 0
        
        for item in items:
            totalAmount += int(item)
        
        if (totalAmount <= 100):
            discount = totalAmount * 0.05
        elif (totalAmount > 100 and totalAmount <= 200):
            discount = totalAmount * 0.10
        elif (totalAmount > 200 and totalAmount <= 500):
            discount = totalAmount * 0.15 
        elif (totalAmount > 500):
            discount = totalAmount * 0.20

        finalAmount = totalAmount - discount

        return render_template("index.html", tot = totalAmount, disc = discount, final = finalAmount)


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000)


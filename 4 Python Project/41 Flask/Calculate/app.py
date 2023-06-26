from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/demo", methods=['POST'])
def arithmetic():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0

        if (operation == "add"):
            result = num1 + num2
        elif (operation == "multiply"):
            result = num1 * num2
        elif (operation == "divide"):
            result = num1 / num2
        elif (operation == "subtraction"):
            result = num1 - num2

        return jsonify(f"The operation is {operation} and the result is {result}")


@app.route("/add", methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if (operation == "add"):
            result = num1 + num2
        elif (operation == "multiply"):
            result = num1 * num2
        elif (operation == "divide"):
            result = num1 / num2
        elif (operation == "subtraction"):
            result = num1 - num2

        # return render_template("result.html", res=result)
        return render_template("index.html", res=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

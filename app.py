from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return f'Hello, {request.args["lastname"]} {request.args["name"]}'
    # return render_template("index.html", name="Andrey", lastname="Pak")
    data = ['1', '2', '3', '4', '5', '6', '7', 8]
    if "name" in request.args:
        return render_template("index.html", name=request.args["name"], lastname=request.args["lastname"],
                               data=data, flag=False)
    else:
        return render_template("index.html", name="Dear", lastname="Guest",
                               data=data, flag=True)

@app.route("/data")
def data():
    return render_template("data.html")



if __name__ == '__main__':
    app.run()

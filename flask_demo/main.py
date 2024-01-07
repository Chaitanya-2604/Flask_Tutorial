from flask import Flask, render_template

app=Flask(__name__)

@app.route('/',methods=["GET"])
def welcome():
    return "<h1 style=color:red> Hello-World</h1>"

@app.route("/index",methods=["GET"])
def student():
    return "Hello! I'm Chaitanya"

@app.route("/login")
def login():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
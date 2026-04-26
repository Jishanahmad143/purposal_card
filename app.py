from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html") 

@app.route('/Yes')   
def yes():
    return render_template("Yes.html")

@app.route('/No')   
def no():
    return render_template("No.html")

if __name__ == '__main__':
    app.run(debug=True)


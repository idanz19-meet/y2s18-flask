from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    a_list = ["Marx","Lenin","Luxembourg"]
    return render_template("index.html", a_list = a_list,  communist = True)
    

if __name__ == '__main__':
   app.run(debug = True)
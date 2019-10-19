from flask import Flask, request, render_template


app = Flask(__name__)

database = list()


# This is the home route
@app.route('/')
def homeRoute():


    return render_template('index.html')








if __name__ == "__main__":
    app.run(debug=True)
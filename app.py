from flask import Flask, request, render_template


app = Flask(__name__)



# This is the home route
@app.route('/', methods=['POST', 'GET'])
def homeRoute():

# get data from createAndEdit route to be display in index.html
    if request.method == "POST":
        form_Infos = request.form

    return render_template('index.html', form_Infos=form_Infos)


# forms route " this route  connects from a href link in the index.html"
# https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm
@app.route('/createAndEdit', methods=['POST', 'GET'])
def createAndEdit():


    return render_template("createAndEdit.html" )





if __name__ == "__main__":
    app.run(debug=True)
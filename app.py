from flask import Flask, request, render_template


app = Flask(__name__)

database = {'notes': 'Note: First day of class',
            'action':'Action: Urgent'}



# This is the home route
@app.route('/note')
def homeRoute():


    return render_template('index.html', database=database)




    





if __name__ == "__main__":
    app.run(debug=True)
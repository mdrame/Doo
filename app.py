from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

database = list()



# This is the home route
@app.route('/')
def homeRoute():


    return render_template('index.html', database=database)




@app.route("/notes/new")
def new_note():

    return render_template('createAndEdit.html')



@app.route("/notes", methods=['POST'])
def notes_submit():

  
    
    database.append(request.form.get('note'))
    database.append(request.form.get('color'))
    database.append(request.form.get('action'))
            
    print(database)
    

    return render_template('index.html', database=database)



    





if __name__ == "__main__":
    app.run(debug=True)
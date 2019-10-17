from flask import Flask, request, render_template


app = Flask(__name__)

database = list()


# This is the home route
@app.route('/', methods=['POST', 'GET'])
def homeRoute():


    return render_template('index.html')


@app.route('/todo')
def todo():

    return render_template('todo.html')


# forms route " this route  connects from a href link in the index.html"
# https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm
@app.route('/create', methods=['POST', 'GET'])
def create():



    return render_template("createAndEdit.html" )

@app.route("/edit")
def edit():

    return render_template("createAndEdit.html")

@app.route('/delete')
def delete():


    return "Delet button press"

@app.route("/edit_Updated")
def edit_Updated():

    return " edits updated return to todo.html"



@app.route('/todo_Action', methods=['POST', 'GET'])
def todo_Action():



    return "render template base of action seleted"



#Rout shoes ever listing created 
@app.route('/notes', methods=['POST', 'GET'])
def notes():

    if request.method == 'POST':

        form_infos = {'color': request.form.get('color'),
                      'text':  request.form.get('comment'),
                      'action':request.form.get('action')}
        # testing
        # print(form_infos['color'])
        # print(form_infos['text'])
        # print(form_infos['action'])
        
        database.append(form_infos)

        return render_template('index.html', database=database)


#View todo list item route
@app.route('/view')
def view():



    return render_template('view.html')









if __name__ == "__main__":
    app.run(debug=True)
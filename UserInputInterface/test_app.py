from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def my_form():
    
    if request.method == 'POST':
	return render_template("page.html",message=request.form['fooput'])
    if request.method == 'GET':
        return render_template("page.html",message="user input is empty until now")

if __name__ == '__main__':
    app.run()

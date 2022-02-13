from flask import render_template,request, redirect, flash
from flask_app import app
from flask_app.models.email import User

@app.route('/create/email', methods=['POST'])
def create():
  if not User.validate_user(request.form):
    flash("Email cannot be blank!", 'email')
    return redirect('/')
  data = {
    "email" : request.form['email'],
  }
  User.save(data)
  return redirect('/success')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success')
def show_info():
  return render_template('results.html', results=User.get_all())
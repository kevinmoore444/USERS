from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User
from flask_app import app




@app.route("/")
def read_all():
    all_users = User.get_all()
    return render_template("user_read_all.html", all_users=all_users)


@app.route("/users/new")
def user_create_form():
    return render_template("user_create.html")

@app.route("/users/add", methods=['POST'])
def add_user():
    id = User.add_user(request.form)
    return redirect(f'/users/{id}/view')

@app.route('/users/<int:id>/view')
def get_one(id):
    data = {
        'id':id
    }
    one_user = User.get_one(data)
    return render_template("user_show_one.html", one_user = one_user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id':id
    }
    one_user = User.get_one(data)
    return render_template("user_edit.html", one_user = one_user)


@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'id' : id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.update_user(data)
    return redirect("/")


@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete({'id':id})
    return redirect('/')





from flask import Flask, render_template, request, redirect
from models.task import Task 

from flask import Blueprint

from repositories import task_repository, user_repository


tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks=tasks)

@tasks_blueprint.route("/tasks/new")
def new_task():
    all_users = user_repository.select_all()
    return render_template("tasks/new.html", all_users=all_users)

@tasks_blueprint.route("/tasks", methods=["POST"])
def create():
    description = request.form['description']
    duration = request.form['duration']
    completed = request.form['completed']
    user_id = request.form['user_id']
    user = user_repository.select(user_id)
    new_task = Task(description, user, duration, completed)
    task_repository.save(new_task)
    return redirect("/tasks")

@tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
def delete(id):
    task_repository.delete(id)
    return redirect("/tasks")

@tasks_blueprint.route("/tasks/<id>/edit")
def edit(id):
    task = task_repository.select(id)
    users = user_repository.select_all()
    return render_template("tasks/edit.html", task=task, all_users=users)

@tasks_blueprint.route("/tasks/<id>", methods=["POST"])
def update(id):
    description = request.form['description']
    duration = request.form['duration']
    completed = request.form['completed']
    user_id = request.form['user_id']
    user = user_repository.select(user_id)
    updated_task = Task(description, user, duration, completed, id)
    task_repository.update(updated_task)
    return redirect("/tasks")
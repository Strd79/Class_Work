from flask import Flask, render_template
from models.animal import Animal 

from flask import Blueprint

from repositories import animal_repository, owner_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.se
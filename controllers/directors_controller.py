from flask import Blueprint, render_template, request, redirect
from repositories import director_repository, video_repository
from models.director import Director
import pdb

directors_blueprint = Blueprint("directors",__name__)

@directors_blueprint.route("/directors")
def directors():
    all_directors = director_repository.select_all()
    return render_template("directors/index.html", all_directors=all_directors)


@directors_blueprint.route("/directors/new")
def new_director():
    return render_template("directors/new.html")


@directors_blueprint.route("/directors", methods=['POST'])
def create_director():
    name = request.form['name']
    contact_number = request.form['contact_number']
    activity = request.form['active']

    director = Director(name, contact_number, activity)
    director_repository.save(director)

    return redirect('/directors')


@directors_blueprint.route("/directors/<id>")
def show_director(id):
    director = director_repository.select(id)
    return render_template("directors/show.html", director=director)

@directors_blueprint.route("/directors/<id>/edit")
def edit_director(id):
    director = director_repository.select(id)
    return render_template("directors/edit.html", director=director)


@directors_blueprint.route("/directors/<int:id>", methods=['POST'])
def update_director(id):
    name = request.form['name']
    contact_number = request.form['contact_number']
    activity = request.form['activity']

    director = Director(name, contact_number, activity, id)
    director_repository.update(director)
    return redirect('/directors')


@directors_blueprint.route("/directors/<id>/delete", methods=["POST"])
def delete_director(id):
    director_repository.delete(id)
    return redirect('/directors')
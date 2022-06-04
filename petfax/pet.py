from flask import (Blueprint, render_template, request)

import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    # return 'This is the pets index'
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show_pet(pet_id):
    pet = pets[pet_id - 1]
    return render_template('show.html', pet=pet)

@bp.route('/new', methods = ['POST', 'GET'])
def new_pet():
    # if request.method == 'POST':
    #     result = request.form
        return render_template('new.html')
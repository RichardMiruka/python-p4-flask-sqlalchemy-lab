#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        response = f'<h2>Animal: {animal.name}</h2>'
        response += f'<ul><li>Species: {animal.species}</li>'
        response += f'<li>Zookeper: {animal.zookeper.name}</li>'
        response += f'<li>Enclosure: {animal.enclosure.environment}</li>'
        return response
    
    else:
        return f'Animal with ID{id} not found'
    

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        response = f'<h2>Zookeeper: {zookeeper.name}</h2>'
        response += f'<ul><li>Birthday: {zookeeper.birthday}</li>'
        response += '<li>Animals:</li><ul>'
        for animal in zookeeper.animals:
            response += f'<li>{animal.name} - {animal.species}</li>'
        response += '</ul><ul>'
        return response 
    else:
        return f'Zookeeper with ID {id} does not exist.'
        
    return ''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        response = f'<h2>Enclosure: {enclosure.environment}</h2>'
        response += f'<ul><li>Open to Visitors: {enclosure.open_visitors}</li>'
        response += '<li>Animals:</li><ul>'
        for animal in enclosure.animals:
            response += f'<li>{animal.name} - {animal.species}</li>'
            response += '</ul></ul>'
            return response
    else:
        return f'Enclosure with ID {id} not found'
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

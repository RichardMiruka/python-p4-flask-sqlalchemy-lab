from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birthday = db.Column(db.Date)
    

    id = db.Column(db.Integer, primary_key=True)
    

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(255), nullable=False)
    open_visitors = db.Column(db.Boolean, default=False)

    id = db.Column(db.Integer, primary_key=True)

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    species = db.Column(db.String(100))
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    zookeeper = db.relationship('Zookeeper', backref=db.backref('animals', lazy=True))
    enclosure = db.relationship('Enclosure', backref=db.backref('animals', lazy=True))
    
    

    id = db.Column(db.Integer, primary_key=True)

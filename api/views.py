from flask import render_template, jsonify,request, send_from_directory
from api import api
from api.models import items_schema,Item,item_schema
from app import db
import os
from datetime import datetime


UPLOAD_DIRECTORY ='./upload'

@api.route('/')
def home():
    return render_template('index.html')
@api.route('/api/')
def show():
    return {
        'messege':'hai'
    }

@api.route('/api/items')
def items_meth():
    items = Item.query.all()
    print(items)
    itm = items_schema.dump(items)
    return jsonify({'items':itm})

@api.route('/api/item', methods=['POST'])
def add_item():
    print(request.json['name'])
    name=request.json['name']
    category=request.json['category']
    price=request.json['price']
    item = Item(name=name,category=category,price=price)
    db.session.add(item)
    db.session.commit()
    return jsonify({'messege':'Success'})

@api.route('/api/item/image', methods=['POST'])
def add_image():
    img = request.files['file']
    print(img)
    filename=str(datetime.now())+img.filename
    img.save(os.path.join(UPLOAD_DIRECTORY,filename))
    return './pics/'+filename,201

@api.route('/pics/<file>')
def accessfile(file):
    return send_from_directory(UPLOAD_DIRECTORY,file)
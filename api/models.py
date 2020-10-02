from api import api
from app import db,ma
# ,app
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = True)
    price = db.Column(db.Integer, nullable = True)
    imgs = db.relationship('Image', backref='item', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    picname = db.Column(db.String, nullable = False)
    person_id = db.Column(db.Integer, db.ForeignKey('item.id'),nullable=False)

# admin = Admin(app)

# # from api.models import Item
# admin.add_view(ModelView(Item,db.session))
class ImageSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ["picname",'id']

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("item_detail", id="<id>"), "collection": ma.URLFor("image")}
    )

class ItemSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","name", "category", "price", 'imgs')
    # imgs = ma.Nested(ImageSchema)
    imgs = ma.Nested(ImageSchema, many = True)
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("item_detail", id="<id>"), "collection": ma.URLFor("item")}
    )


item_schema = ItemSchema()
items_schema = ItemSchema(many = True)

# image_schema = ImageSchema()
image_schema = ImageSchema(many = True)

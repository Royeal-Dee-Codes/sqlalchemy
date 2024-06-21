import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.products_categories_xref import products_categories_xref


class Categories(db.Model):
    __tablename__ = "Categories"

    category_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_name = db.Column(db.String(), nullabl=False)

    products = db.relationship('Products', back_populates='categories', secondary=products_categories_xref)

    def __init__(self, category_name):
        self.category_name = category_name

    def new_category_obj():
        return Categories("")


class CategoriesSchema(ma.Schema):

    class Meta:
        fields = ['category_id', 'category_name']
    categories = ma.fields.Nested("CategoriesSchema")


category_schema = CategoriesSchema()
categories_schema = CategoriesSchema()

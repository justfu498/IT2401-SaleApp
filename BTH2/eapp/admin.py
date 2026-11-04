from flask_admin.contrib.sqla import ModelView

from eapp.models import Category, Product
from eapp import app, db
from flask_admin import Admin

admin = Admin(app=app, name='E-Commerce Admin')

class ProductView(ModelView):
    column_list = ['id', 'name', 'active', 'category_id']
    column_searchable_list = ['name']


admin.add_view(ProductView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
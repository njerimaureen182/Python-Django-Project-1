# django.db is a package that contains the 'models' module
# the 'models' module contains fields and behaviour of the data you are storing
# each model maps to a single database table
# each model is a python class that subclasses django.db.models.Model
# each attribute of the model represents a database field
from django.db import models

# let's create a new class called 'Product':


class Product(models.Model):

    # let's define attributes in this class, e.g name, price, stock, image etc
    # 1. the 'name' attribute
    # charField = a field that can contain textual data
    # we've set the maximum length of the character field to be 255
    name = models.CharField(max_length=255)
    # the price attribute:
    price = models.FloatField()
    # the stock attribute:
    stock = models.IntegerField()
    # the image attribute whose standard max length for urls is 2083
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):

    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()





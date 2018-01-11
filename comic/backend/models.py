from django.db import models
from django.conf import settings
from mongoengine import *


class Pokemon(Document):
    id = StringField()
    _id = StringField()
    comic_name = StringField()
    number = StringField()
    name_cn = StringField()
    name_jp = StringField()
    name_en = StringField()
    page_url = StringField()
    img_url = StringField()
    local_img_path = StringField()
    meta = {'collection': 'pokemon'}
# Create your models here.

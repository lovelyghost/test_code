# -*- coding:utf-8 -*-
from mongoengine import connect, Document, StringField, ReferenceField

connect('project1')
from mongoengine import *


class Page(DynamicDocument):
    title = StringField(max_length=200, required=True)

# Create a new page and add tags
page = Page(title='Using MongoEngine')
page.tags = ['mongodb', 'mongoengine']
page.save()

print(Page.objects(tags='mongoengine').count())


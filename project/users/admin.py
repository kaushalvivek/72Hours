# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item, User

# Register your models here.
admin.site.register(Item)
admin.site.register(User)
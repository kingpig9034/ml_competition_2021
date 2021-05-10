# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from was_rest.models import *

myModels = [Profile, Score]
admin.site.register(myModels)
# Register your models here.
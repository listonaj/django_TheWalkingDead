from django.contrib import admin

# Register your models here.
# don't forget the dot in front of <models>, it tells django to look for models.py
from .models import Topic

# tells Django to manage the model through the admin site
admin.site.register(Topic)
from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Property)
admin.site.register(Price)
admin.site.register(Yelp_Details)
admin.site.register(Yelp)


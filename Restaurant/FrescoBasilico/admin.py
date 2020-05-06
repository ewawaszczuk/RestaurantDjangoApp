from django.contrib import admin
from .models import Meals

admin.site.site_header = 'Fresco Basilico Admin Panel'

class MealsAdmin(admin.ModelAdmin):
    list_display = ("name",'ingredients','price', 'type_of_food' )




admin.site.register(Meals, MealsAdmin)

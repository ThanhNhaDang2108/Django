from django.contrib import admin

# Register your models here.
from .models import ThanhNha, Recipe
admin.site.register(ThanhNha)
admin.site.register(Recipe)
from django.contrib import admin

# Register your models here. Modules are registered here to give the admin control
from .models import Board, Review

admin.site.register(Board)
admin.site.register(Review)

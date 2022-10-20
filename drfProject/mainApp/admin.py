from django.contrib import admin
from .models import Member, Review, Coffee

# Register your models here.
admin.site.register(Review)
admin.site.register(Coffee)
admin.site.register(Member)
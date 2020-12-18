from django.contrib import admin
# Register your models here.
from cos.models import Book # NEW
admin.site.register(Book) # NEW

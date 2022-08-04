from ast import Import
from pkgutil import ImpImporter
from django.contrib import admin

# Register your models here.

from .models import celebrity,bookings,book,author
admin.site.register(celebrity)
admin.site.register(bookings)
admin.site.register(author)
admin.site.register(book)
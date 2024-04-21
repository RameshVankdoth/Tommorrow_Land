from django.contrib import admin
from .models import electronics,gaming,movie,vehicles,products
admin.site.register(products)
admin.site.register(electronics)
admin.site.register(gaming)
admin.site.register(vehicles)
admin.site.register(movie)
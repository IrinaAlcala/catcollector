from django.contrib import admin
from .models import Cat, Feeding

admin.site.register(Cat)
# Register your models here.
admin.site.register(Feeding)
from django.contrib import admin

# Register your models here.
from .models import Level1, Level2, Level3
admin.site.register(Level1)
admin.site.register(Level2)
admin.site.register(Level3)

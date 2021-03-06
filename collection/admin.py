from django.contrib import admin

from .models import Mineral, Image

class ImageAdmin(admin.TabularInline):
    model = Image

class MineralAdmin(admin.ModelAdmin):
    inlines = [
            ImageAdmin
    ]
   

admin.site.register(Mineral, MineralAdmin)

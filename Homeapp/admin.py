from django.contrib import admin
from.models import *
from .models import Blog



admin.site.register(Carausel)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Gallery)


@admin.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinymce.js',)
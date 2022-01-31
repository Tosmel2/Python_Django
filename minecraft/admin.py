from django.contrib import admin

from minecraft.models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']


admin.site.register(Category)





admin.site.register(Blog, BlogAdmin)
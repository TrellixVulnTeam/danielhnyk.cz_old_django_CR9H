from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted', 'last_mod']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posted', 'publish')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


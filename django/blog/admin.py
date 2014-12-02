from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted', 'last_mod']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posted', 'publish', 'get_category_title')

    def get_category_title(self, obj):
        return obj.category.title
    get_category_title.short_description = "Category"
    get_category_title.admin_order_field = "category__title"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


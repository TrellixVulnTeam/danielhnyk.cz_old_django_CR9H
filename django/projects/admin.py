from django.contrib import admin

from projects.models import Project, PClass

class ProjectAdmin(admin.ModelAdmin):
    exclude = ['start', 'last_mod']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'start')

class PClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(PClass, PClassAdmin)

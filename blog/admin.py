from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date']
    list_display_links = ['description', 'date']
    search_fields = ['title', 'slug', 'description']
    actions = ['activate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)


# Register your models here.
admin.site.register(Blog, BlogAdmin)

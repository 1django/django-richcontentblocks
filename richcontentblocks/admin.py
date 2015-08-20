from django.contrib import admin
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_group', 'key', 'updated', )
    search_fields = ('title', 'content', )
    list_filter = ('content_group', 'created', 'updated')
    readonly_fields = ('created', 'updated', 'key',)
    ordering = ('content_group',)

admin.site.register(Content, ContentAdmin)

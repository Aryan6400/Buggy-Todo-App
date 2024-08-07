from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'title', 'body', 'created_at', 'updated_at')
    ordering = ('-updated_At',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Todo, TodoAdmin)
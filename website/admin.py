from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'time', 'completed', 'created_at')
    list_filter = ('completed', 'date', 'user')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'date'
    ordering = ('-date', '-created_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Task Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Schedule', {
            'fields': ('date', 'time')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

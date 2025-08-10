from django.contrib import admin
from .models import Task, UserProfile

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'is_completed', 'due_date', 'created_at')
    list_filter = ('priority', 'status', 'is_completed', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'user__username', 'user__first_name', 'user__last_name')
    list_editable = ('priority', 'status', 'is_completed')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'user')
        }),
        ('Status & Priority', {
            'fields': ('priority', 'status', 'is_completed')
        }),
        ('Dates', {
            'fields': ('due_date', 'created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at', 'completed_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'get_full_name')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('date_of_birth',)
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Full Name'

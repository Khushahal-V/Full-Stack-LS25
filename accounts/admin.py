from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'created_at')
    search_fields = ('user__username', 'user__email')
    ordering = ('-created_at',)

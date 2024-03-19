from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Permission

from user.models import *



# Register your models here.
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('user_type',)  # Enable search by user type
    readonly_fields = ('id', 'created_at', 'updated_at')  # Make certain fields read-only
    list_filter = ('created_at', 'updated_at')  # Add list filters for created_at and updated_at
    actions = ['mark_as_provider', 'mark_as_customer']  # Custom admin actions

    fieldsets = (
        ('User Type Info', {
            'fields': ('user_type',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Make timestamps collapsible
        }),
    )

    def mark_as_provider(self, request, queryset):
        rows_updated = queryset.update(user_type='provider')
        self.message_user(request, f'{rows_updated} user type(s) marked as provider.')

    mark_as_provider.short_description = 'Mark selected as Provider'

    def mark_as_customer(self, request, queryset):
        rows_updated = queryset.update(user_type='customer')
        self.message_user(request, f'{rows_updated} user type(s) marked as customer.')

    mark_as_customer.short_description = 'Mark selected as Customer'

admin.site.register(UserType, UserTypeAdmin)
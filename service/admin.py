from django.contrib import admin
from service.models import *
# Register your models here.
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by name
    readonly_fields = ('id', 'created_at', 'updated_at')  # Make certain fields read-only
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Make the timestamps collapsible
        }),
    )


    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ServiceCategory, ServiceCategoryAdmin)

class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'provider', 'price', 'active', 'created_at', 'updated_at')
    list_filter = ('category', 'provider', 'active')
    search_fields = ('title', 'desc')
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'provider', 'price', 'active', 'desc', 'address', 'picture')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ProviderService, ProviderServiceAdmin)
from django.contrib import admin
from info_pages.models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Additional Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Makes this fieldset collapsible
        })
    )

    def has_delete_permission(self, request, obj=None):
        return False  # Disable delete permission for ContactUs objects

admin.site.register(ContactUs, ContactUsAdmin)

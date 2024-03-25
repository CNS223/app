from django.contrib import admin
from info_pages.models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone', 'message')

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('message',)
        }),
       
    )

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(ContactUs, ContactUsAdmin)

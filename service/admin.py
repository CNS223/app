from django.contrib import admin
from service.models import *


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


class ProviderAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'available', 'start_time', 'end_time', 'service', 'created_at', 'updated_at')
    list_filter = ('day', 'available', 'service')
    search_fields = ('day', 'service__title')
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('day', 'available', 'start_time', 'end_time', 'service')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ProviderAvailability, ProviderAvailabilityAdmin)




class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'status', 'appointment_time', 'address', 'price', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'service__title', 'appointment_time')
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'service', 'status', 'appointment_time', 'address', 'price')
        }),
        ('Additional Information', {
            'fields': ('desc',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ServiceBooking, ServiceBookingAdmin)




class ServiceRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'rate', 'comment', 'created_at', 'updated_at')
    list_filter = ('rate', 'created_at', 'updated_at')
    search_fields = ('service__id', 'comment')
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('service', 'rate', 'comment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ServiceRating, ServiceRatingAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'feedback')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user','feedback')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
admin.site.register(Feedback, FeedbackAdmin)
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Permission

from user.models import *


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


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('content_type')

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_active', 'is_admin', 'is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'email', 'phone_number','first_name', 'last_name', 'is_admin', 'email_verified',  'last_login')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone_number','password', 'email_verified')}),
        ('Profile Picture', {'fields': ('avatar',)}),
        ('Additional Info', {'fields': ('first_name', 'last_name','bio', 'experience', 'user_type', 'gender', 'currency_code')}),
        ('Permissions', {'fields': ('is_staff', 'is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
    )
    admin.site.disable_action('delete_selected')
    search_fields = ('username', 'email')
    ordering = ('id',)

    filter_horizontal = ()

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


admin.site.register(User, UserAdmin)



class ProviderGetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'provider', 'full_name', 'email', 'phone_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'provider__username', 'full_name', 'email', 'phone_number')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'provider', 'full_name', 'email', 'phone_number', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Make the timestamps collapsible
        }),
    )

admin.site.register(ProviderGetInTouch, ProviderGetInTouchAdmin)

class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_to', 'verification_token', 'validity')
    list_filter = ('validity',)
    search_fields = ('email_to__username',)
    readonly_fields = ('id', 'validity')
    fieldsets = (
        (None, {
            'fields': ('email_to', 'verification_token')
        }),
        ('Validity', {
            'fields': ('validity',),
            'classes': ('collapse',)  # Make the validity field collapsible
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False 
admin.site.register(EmailVerification, EmailVerificationAdmin)



class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'add1', 'city', 'address_type', 'provision', 'country', 'postal_code','created_at', 'updated_at')
    list_filter = ('address_type', 'provision', 'country', 'created_at', 'updated_at')
    search_fields = ('add1', 'city', 'postal_code',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('add1', 'add2', 'city', 'address_type', 'provision', 'country', 'postal_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Address, AddressAdmin)

class UserSystemVisitAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'daily_count', 'total_count')
    readonly_fields = ('created_at', 'daily_count', 'total_count')
    search_fields = ('created_at',)
    date_hierarchy = 'created_at'

admin.site.register(UserSystemVisit, UserSystemVisitAdmin)
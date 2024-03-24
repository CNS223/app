from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def custom_message(message):
    return format_html('<div class="custom-message">{}</div>', message)

@register.simple_tag
def custom_notification(message, notification_type='info'):
    return f"""
    <div class="alert alert-{notification_type} alert-dismissible fade show" role="alert">
        {message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    """
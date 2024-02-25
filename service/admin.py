from django.contrib import admin
from service.models import *
# Register your models here.
admin.site.register(UserServiceRating)
admin.site.register(UserService)
admin.site.register(ServicePost)
admin.site.register(ServiceCategory)
admin.site.register(ServicePostComment)
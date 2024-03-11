from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Collection, Payment

admin.site.register(Collection)
admin.site.register(Payment)
admin.site.unregister(Group)

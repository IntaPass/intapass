from django.contrib import admin

from .models import Access, SSHKeys

admin.site.register(Access)
admin.site.register(SSHKeys)
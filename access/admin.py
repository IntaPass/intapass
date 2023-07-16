from django.contrib import admin

from .models import Access, SSHKeys

@admin.action(description="Grant access")
def grant_access(modeladmin, request, queryset):
    for item in queryset.all():
        item.add_key_to_host()

class AccessAdmin(admin.ModelAdmin):
    actions = [grant_access, ]

admin.site.register(Access, AccessAdmin)
admin.site.register(SSHKeys)
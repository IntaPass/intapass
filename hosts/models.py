from django.db import models

class Host(models.Model):
    label = models.SlugField(unique=True, max_length=45, help_text="Server name or identifier")
    ip_address = models.GenericIPAddressField()
    ssh_port = models.IntegerField(default=22)
    ssh_user = models.CharField(max_length=32, default="root", help_text="Default user")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.label} - {self.ip_address}"
    
    class Meta:
        ordering = ("-created_at", )
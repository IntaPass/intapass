from django.db import models

class Host(models.Model):
    label = models.SlugField(unique=True, max_length=45, help_text="Server name or identifier")
    ip_address = models.GenericIPAddressField()
    ssh_port = models.IntegerField(default=22)
    ssh_user = models.CharField(max_length=32, default="root", help_text="Default user")

    def __str__(self) -> str:
        return f"{self.label} - {self.ip_address}"
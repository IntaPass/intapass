from django.db import models

class Host(models.Model):
    ip_address = models.IPAddressField()
    ssh_port = models.IntegerField(default=22)
    ssh_user = models.CharField(max_length=32, default="root", help_text="Default user")

    def __str__(self) -> str:
        return f"{self.ip_address}"
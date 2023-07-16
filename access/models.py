from django.db import models

from worker import manage

class SSHKeys(models.Model):
    owner = models.ForeignKey("auth.User", related_name="ssh_keys", on_delete=models.PROTECT)
    label = models.CharField(max_length=32, default="default")
    pub_key = models.TextField()

    def __str__(self) -> str:
        return f"{self.label} ({self.owner})"


class Access(models.Model):
    GRANTED = "GRANTED"
    REMOVED = "REMOVED"
    PENDING = "PENDING"
    FAILED = "FAILED"

    STATUSES = (
        (PENDING, PENDING),
        (GRANTED, GRANTED),
        (REMOVED, REMOVED),
        (FAILED, FAILED),
    )

    host = models.ForeignKey("hosts.Host", related_name="accesses", on_delete=models.PROTECT)
    ssh_key = models.ForeignKey(SSHKeys, related_name="accesses", on_delete=models.PROTECT)
    status = models.CharField(max_length=15, choices=STATUSES, default=PENDING)

    def __str__(self) -> str:
        return f"{self.status} {self.ssh_key} - {self.host}"

    def add_key_to_host(self):
        """
        Add SSH Key to host
        """
        worker = manage.Worker()
        worker.give_access([self.ssh_key, ], [self.host, ])

    def remove_key_from_host(self):
        """
        Remove SSH Key from host
        """
        pass
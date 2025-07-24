from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view document"),
            ("can_create", "Can create document"),
            ("can_edit", "Can edit document"),
            ("can_delete", "Can delete document"),
        ]

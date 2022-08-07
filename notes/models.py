from django.db import models


class Note(models.Model):
    # title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
    
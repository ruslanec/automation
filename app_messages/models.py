from django.db import models


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    owner = models.ForeignKey('account.Account', related_name='messages')

    class Meta:
        ordering = ('created',)


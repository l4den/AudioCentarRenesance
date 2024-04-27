from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    email = models.EmailField(max_length=150)
    subject = models.CharField(_('Subject'), max_length=150)
    message = models.TextField(_('Message'), max_length=255)
    date_sent = models.DateTimeField(_('Date_created'), auto_now_add=True, null=True)

    class Meta:
        verbose_name = _('ContactMessage')
        verbose_name_plural = _('ContactMessages')

    def __str__(self):
        return f'{self.subject} - {self.email}'


class NewsLetter(models.Model):
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('NewsLetter')
        verbose_name_plural = _('NewsLetters')

    def __str__(self):
        return self.email

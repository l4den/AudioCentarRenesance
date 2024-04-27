from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import ContactMessage
from django.core.mail import send_mail
from django.utils import timezone


@receiver(post_save, sender=ContactMessage)
def create_token(sender, instance, created, **kwargs):
    print('signal function called')
    
    if created:
        
        subject = instance.subject
        message = f"""
                                    {instance.message}

                                    From:
                                    {instance.email}
                                    """
        sender = 'audiocentarrenesansa@gmail.com'
        receiver = ['stefan.ladinski.work@gmail.com', ]
        # caraudio@t.mk

        send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False
        )
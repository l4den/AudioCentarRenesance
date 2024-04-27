from django.contrib import admin
from .models import ContactMessage, NewsLetter

class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ('email', 'subject', 'get_date_sent')

    def get_date_sent(self, obj):
        return obj.date_sent.strftime('%d %B, %Y, %H:%M')
    get_date_sent.short_description = 'Date Sent'


admin.site.register(NewsLetter)
admin.site.register(ContactMessage, ContactMessageAdmin)

# Register your models here.

from django.contrib import admin
from .models import SubscribedToNewsletter, ContactUs, ContactUsForm

# Register your models here.
@admin.register(SubscribedToNewsletter)
class SubscribedToNewsletterAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactUsForm)
class ContactUsFormAdmin(admin.ModelAdmin):
    pass


    

    

    


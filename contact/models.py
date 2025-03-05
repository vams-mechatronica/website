from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class ContactUsForm(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("ContactUsForm")
        verbose_name_plural = _("ContactUsForm")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContactUsForm_detail", kwargs={"pk": self.pk})

class ContactUs(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.TextField(_("Address"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContactUs_detail", kwargs={"pk": self.pk})

class SubscribedToNewsletter(models.Model):
    email = models.EmailField(_("Email"), max_length=254)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    

    class Meta:
        verbose_name = _("SubscribedToNewsletter")
        verbose_name_plural = _("SubscribedToNewsletters")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("SubscribedToNewsletter_detail", kwargs={"pk": self.pk})



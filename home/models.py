from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class Index(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    slogan = models.CharField(_("Slogan"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="index/logo/",null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to="index/",null=True, blank=True)
    youtube_link = models.CharField(_("Youtube Link"), max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)  
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True) 
    class Meta:
        verbose_name = _("Index")
        verbose_name_plural = _("Indexs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Index_detail", kwargs={"pk": self.pk})

class FAQ(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="faq/")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("FAQ_detail", kwargs={"pk": self.pk})


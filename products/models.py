from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class ProductORService(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="productorservice/")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("ProductORService")
        verbose_name_plural = _("ProductORServices")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductORService_detail", kwargs={"pk": self.pk})

class Feature(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="feature/")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Feature_detail", kwargs={"pk": self.pk})


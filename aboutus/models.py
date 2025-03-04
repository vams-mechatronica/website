from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class AboutUs(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="aboutus/")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("AboutUs")
        verbose_name_plural = _("AboutUss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AboutUs_detail", kwargs={"pk": self.pk})


class Team(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    designation = models.CharField(_("Designation"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="team/")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})


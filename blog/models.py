from django.db import models
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(_("title"), max_length=250)
    author = models.CharField(_("Author"), max_length=250)
    category = models.CharField(_("Category"), max_length=50,null=True,blank=True)
    image_url = models.ImageField(_("Blog Image"), upload_to="blog/",null=True,blank=True)
    content = QuillField()
    date = models.DateField(_("Date Posted"), auto_now=False, auto_now_add=False)
    post_url = models.CharField(_("Blog Url"), max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(_("Created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated_at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})

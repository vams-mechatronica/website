from django.db import models
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField
from django.urls import reverse

class BlogCategories(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    class Meta:
        verbose_name = _("BlogCategories")
        verbose_name_plural = _("BlogCategories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BlogCategories_detail", kwargs={"pk": self.pk})

class BlogTag(models.Model):
    name = models.CharField(_("Tags"), max_length=50)
    category = models.ForeignKey(BlogCategories, verbose_name=_("Category"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("BlogTag")
        verbose_name_plural = _("BlogTags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BlogTag_detail", kwargs={"pk": self.pk})

# Create your models here.
class Blog(models.Model):
    title = models.CharField(_("title"), max_length=250)
    author = models.CharField(_("Author"), max_length=250)
    author_role = models.CharField(_("Author Role"), max_length=250, null=True, blank=True)
    category = models.ForeignKey(BlogCategories, verbose_name=_("category"), on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ForeignKey(BlogTag, verbose_name=_("Tag"), on_delete=models.SET_NULL, null=True, blank=True)
    image_url = models.ImageField(_("Blog Image"), upload_to="blog/",null=True,blank=True)
    content = QuillField()
    date = models.DateField(_("Date Posted"), auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(_("is Active"),default=True)
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



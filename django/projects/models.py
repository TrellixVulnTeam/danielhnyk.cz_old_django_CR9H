from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from markupfield.fields import MarkupField

def get_name_file(instance, filename):
    strge = 'pictures/projects/' + str(instance.slug) + filename[-4:]
    return(strge)

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = MarkupField(markup_type="ReST")
    slug = models.SlugField(max_length=100, unique=True)
#    body = models.TextField()
    start = models.DateField(db_index=True, auto_now_add=True)
    last_mod = models.DateField(auto_now=True)
    body_marked = MarkupField(markup_type="ReST")
    end = models.DateField(db_index=True, auto_now_add=True)
    pclass = models.ForeignKey('projects.PClass')
    publish = models.BooleanField(default=False, verbose_name="Should I publish it?")
    title_pic = ThumbnailerImageField(
        upload_to=get_name_file,
        null=True, blank=True,
        verbose_name="Titulní foto")

class PClass(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    pclass_pic = ThumbnailerImageField(
        upload_to=get_name_file,
        verbose_name="Foto kategorie")

    def __str__(self):
        return self.title

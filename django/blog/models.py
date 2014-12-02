from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from markupfield.fields import MarkupField
import os

def get_name_file(instance, filename):
    strge = os.path.join('blog', str(instance.slug), filename)
    return(strge)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
#    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    last_mod = models.DateField(auto_now=True)
    category = models.ForeignKey('blog.Category')
    body_marked = MarkupField(markup_type="ReST")
    publish = models.BooleanField(default=False, verbose_name="Should I publish it?")

    files = models.FileField(upload_to=get_name_file, blank=True)
    
    title_pic = ThumbnailerImageField(
        upload_to=get_name_file,
        default="/media/pictures/blog/template.jpg",
        verbose_name="Titulní foto")


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    categ_pic = ThumbnailerImageField(
        upload_to=get_name_file,
        default="/media/pictures/blog/template.jpg",
        verbose_name="Foto kategorie")

    def __str__(self):
        return self.title

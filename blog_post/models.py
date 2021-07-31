from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.auth.models import User
from sotuvapp.models import UserDetail
from datetime import datetime
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post_categories(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='Sarlavha')
    post_img = models.ImageField(upload_to='rasmlar/post')
    categorie = models.ManyToManyField(Post_categories, null=True, blank=True)
    text_body1 = RichTextUploadingField(blank=True)
    post_img2 = models.ImageField(upload_to='rasmlar/post')
    post_img3 = models.ImageField(upload_to='rasmlar/post')
    text_body2 = RichTextUploadingField(blank=True)
    date = models.DateField(default=datetime.now(), blank=True)
    time = models.TimeField(auto_now_add=True, verbose_name='vaqt')
    slug = models.SlugField(unique=True, max_length=300)
    tags = TaggableManager()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    post_view = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date', '-time']
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Commit(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    reply = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="replies")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name

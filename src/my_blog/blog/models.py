from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class post(models.Model):
    post_subject = models.CharField(max_length = 100)
    post_content = models.TextField()
    post_published = models.DateTimeField(default = timezone.now) 
    post_update = models.DateTimeField(auto_now = True)
    post_author = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
       return self.post_subject

    class Meta:
        ordering = ('-post_published',) 


class Comment(models.Model):
    com_pers_name = models.CharField(max_length = 50)
    com_pers_email = models.EmailField()
    com_content = models.TextField()
    com_published =models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    item = models.ForeignKey(post, on_delete=models.CASCADE ,related_name='comments')
    
    def __str__(self):
        return ' علق {} على {}.'.format(self.com_pers_name , self.item)

    class Meta:
        ordering = ('-com_published',)
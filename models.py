from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='images')
    liked = models.ManyToManyField(User,default=None, blank=True,related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')

    def _str_(self):
        return  str(self.title)

    def num_likes(self):
        return self.liked.all().count()



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    post = models.ForeignKey(User, on_delete=models.CASCADE,related_name='post')
    value = models.CharField(choices = LIKE_CHOICES, default='Like', max_length=20)

    def _str_(self):
        return str(self.post)



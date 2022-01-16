from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, timezone
# Create your models here.
from embed_video.fields import EmbedVideoField

class Post(models.Model):
    ADVANTAGE1 = 'advantage1'
    POST = 'post'
    ADVANTAGE2 = 'advantage2'
    ADVANTAGE3 = 'advantage3'
    ABOUT = 'about'
    JOHNHENRY = 'johnhenry'
    JAYZOONA = 'jayzoona'
    TIMYCAKE = 'timycake'
    CATHERINESOFT = 'catherinesoft'

    CHOISE_GROUP = {
        (JOHNHENRY, 'johnhenry'),
        (JAYZOONA, 'jayzoona'),
        (TIMYCAKE,'timycake'),
        (CATHERINESOFT, 'catherinesoft'),
        (ABOUT, 'about'),
        (ADVANTAGE1, 'advantage1'),
        (POST, 'post'),
        (ADVANTAGE2, 'advantage2'),
        (ADVANTAGE3, 'advantage3'),
    }

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    grop = models.CharField(max_length=20, choices=CHOISE_GROUP, default=POST)
    likes = models.ManyToManyField(User, related_name='blog_posts')





    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def __str__(self):
        return f'{self.title}'




class Contact(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   message = models.TextField()
   timestamp = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.first_name + " - "+ self.last_name



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

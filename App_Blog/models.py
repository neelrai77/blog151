from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length =264, verbose_name="Put a title")
    slug= models.SlugField(max_length= 264, unique=True)
    blog_content = models.TextField(verbose_name= 'what should be the content ?')
    blog_image = models.ImageField(upload_to='blog_images',verbose_name='Blog_Image')
    publish_date=models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    

from django.db import models 
from django.utils import timezone 
from django.urls import reverse
from django.contrib.auth.models import User
 
 
class Category(models.Model): 
    name = models.CharField(max_length = 255,blank = True,null = True)
    def __str__(self): 
        return self.name 
 
class News(models.Model): 
    class Status(models.TextChoices): 
        yuklash = 'S','Successfully' 
        qoralama = "F","Fail " 
    name = models.CharField(max_length=255,blank=True,null=True) 
    text = models.TextField() 
    slug = models.SlugField() 
    image = models.ImageField(upload_to='NewsWeb/image') 
    created_time = models.DateTimeField(auto_now_add=True) 
    upload_time = models.DateTimeField(default=timezone.now) 
    updated_time = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    status = models.CharField(max_length =1,choices=Status.choices,default= Status.qoralama) 
 
 
    def __str__(self): 
        return self.name
    
    def get_absolute_url(self):
        return reverse('news')
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    
    
    def __str__(self):
        return self.name
    
# from django.contrib.auth.models import User

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                             related_name='comments')  
    body = models.TextField() 
    upload_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-upload_time']
          
    def __str__(self) -> str:
        return f"Komment - {self.body}| User: {self.user}."
    
from django.db import models

# Create your models here.
class Post(models.Model):
     
     title = models.CharField(max_length=200,null=True,blank=True)

     content=models.TextField(null=True,blank=True)
    
     img = models.ImageField(upload_to='images', null=True, blank=True)
     
     created = models.DateTimeField(auto_now_add=True)

     class Meta:
         ordering = ('-created',)

     def __str__(self):
        return self.title
class cont(models.Model):
     
     NAME = models.CharField(max_length=200,null=True,blank=True)

     MESSAGE=models.TextField(null=True,blank=True)
    
     
     
     created = models.DateTimeField(auto_now_add=True)

     class Meta:
         ordering = ('-created',)

     def __str__(self):
        return self.title

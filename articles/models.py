from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'
class Articles(models.Model):
    title = models.CharField(max_length=200)  #默认可以为空
    sub_title =  models.CharField(max_length=200,null=True,blank=True)
    key_words = models.CharField(max_length=1024,null=True,blank=True)
    description = models.CharField(max_length=2048,null=True,blank=True)
    article_type = models.SmallIntegerField(default=0)
    is_hot = models.BooleanField(default=False)
    is_published=models.BooleanField(default=False)
    image = models.CharField(max_length=2048,null=True,blank=True)
    image_title = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)

    user = models.ForeignKey(User,related_name='articles_user_set',on_delete=models.CASCADE,default=None,blank=True,null=True)


    class Meta:
        db_table='articles'



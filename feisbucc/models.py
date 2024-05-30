from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,null=True, blank=True,default='vuoto')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(default='profile/blank-profile-picture.png',upload_to='profile/')
    mail = models.EmailField(blank=True)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
            return str(self.user)
    
    def n_followere(self):
        return self.follows.count()
    
    def n_following(self):
        profiles = Profile.objects.all()
        n = 0
        for p in profiles:
            foll = p.follows.all()
            for k in foll:
                if k.user.username == str(self.user):
                    n = n+1
        return n-1

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
        

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    image_post = models.ImageField(null=True, blank=True, upload_to="images/")
    likes = models.ManyToManyField(User, related_name='blog_posts',blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def get_profilePic(self):
        profiles = Profile.objects.all()
        for p in profiles:
            if p.user.username == str(self.author):
                return p.profile_pic
    

    def __str__(self):
        return str(self.author)
    

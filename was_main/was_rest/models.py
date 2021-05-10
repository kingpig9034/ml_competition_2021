from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.get_username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Score(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null = False, related_name = 'scores')
    company = models.CharField(max_length = 100, blank=True, null=True)
    score = models.FloatField(null=True)
    file = models.FileField(upload_to='answers/')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cam_id)

    def save(self, *args, **kwargs):
        super(Score, self).save(*args, **kwargs)
        print('[TIME : %s] Score save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Score, self).delete(*args, **kwargs)
        print('[TIME : %s] Score delete' % str(datetime.now())) 



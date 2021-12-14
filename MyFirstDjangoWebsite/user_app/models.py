from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #The on_delete method is used to tell Django what to do with model instances
    #that depend on the model instance you delete. (e.g. a ForeignKey relationship).
    #The on_delete=models. CASCADE tells Django to cascade the deleting effect
    #i.e. continue deleting the dependent models as well.

    #additional fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

from django.db import models

# superuser: name-luqu email-nadim03akhtar@gmail.com password-mylu8666

# 1. python manage.py migrate
# 2. python manage.py makemigrations app_name
# 3. python manage.py migrate

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

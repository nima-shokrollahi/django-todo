from django.db import models
from django.contrib.auth.models import User
import datetime


class Do(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(null=True,blank=True)
    date_view = models.CharField(default=None, blank=True, null=True, max_length=100)
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwarg):
    #     time = datetime.datetime.now()
    #     print(time.day)
    #     print(self.date.day)
    #     year = self.date.year - time.year
    #     month = self.date.month - time.month
    #     day = self.date.day - time.day
    #     self.date_view = f'{year}:{month}:{day}'
    #     super().save(*args, **kwarg)

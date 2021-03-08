from django.db import models

class File(models.Model):
    name = models.CharField(max_length=200)
    fileId = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name

class TempFile(models.Model):
    file = models.FileField(upload_to='documents/')

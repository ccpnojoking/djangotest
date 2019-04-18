from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.btitle

class RoleInfo(models.Model):
    rname = models.CharField(max_length=20)
    rgender = models.BooleanField()
    rcontent = models.CharField(max_length=50)
    rbook = models.ForeignKey("BookInfo",on_delete=models.CASCADE)
    def __str__(self):
        return self.rname



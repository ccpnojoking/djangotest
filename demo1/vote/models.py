from django.db import models

# Create your models here.

class Questions(models.Model):
    qcontent = models.CharField(max_length=100)
    qpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.qcontent
    def Qcontent(self):
        return self.qcontent
    Qcontent.short_description = "问题"
    def Qpub_date(self):
        return self.qpub_date
    Qpub_date.short_description = "提出时间"

class Answers(models.Model):
    acontent = models.CharField(max_length=100)
    acount = models.IntegerField(max_length=100)
    aquestion = models.ForeignKey("Questions",on_delete=models.CASCADE)
    def __str__(self):
        return self.acontent
    def Acontent(self):
        return self.acontent
    Acontent.short_description = "回答"
    def Acount(self):
        return self.acount
    Acount.short_description = "计数"
    def Aquestion(self):
        return self.aquestion
    Aquestion.short_description = "问题"

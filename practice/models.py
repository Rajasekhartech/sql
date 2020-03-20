from django.db import models

# Create your models here.

class sample(models.Model):
    Name = models.CharField(max_length=20)
    grade = models.IntegerField()

    def __str__(self):
        return self.Name
class markslist(models.Model):
    student = models.OneToOneField(sample, on_delete= models.CASCADE)
    tel = models.IntegerField(max_length=3,blank= True, null= True)
    hin =  models.IntegerField(max_length=3,blank= True, null= True)
    eng = models.IntegerField(max_length=3,blank= True, null= True)
    sci = models.IntegerField(max_length=3,blank= True, null= True)
    soc = models.IntegerField(max_length=3,blank= True, null= True)
    mat = models.IntegerField(max_length=3,blank= True, null= True)

    def __str__(self):

        return self.student.Name


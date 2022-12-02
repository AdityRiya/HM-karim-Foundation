from django.db import models

# Create your models here.
class Executive_Counsil(models.Model):
    ec_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.ec_name
class EC_Post(models.Model):
    name = models.ForeignKey('Executive_Counsil',
    on_delete=models.CASCADE)
    ec_post = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.ec_post
class EC_Number(models.Model):
    
    post = models.ForeignKey('EC_Post',
    on_delete=models.CASCADE)
    ec_number = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.ec_number 
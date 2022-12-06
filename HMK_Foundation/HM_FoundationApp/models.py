from django.db import models

# Create your models here.
class Executive_Counsil(models.Model):
    ec_name = models.CharField(max_length=264)
    ec_post = models.CharField(max_length=264,null=True)
    ec_number = models.CharField(max_length=264,null=True)
    def __str__(self):
        return self.ec_name
        return self.ec_post
        return self.ec_number
class Adviser_Counsil(models.Model):
    ac_name = models.CharField(max_length=264)
    ac_post = models.CharField(max_length=264,null=True)
    ac_number = models.CharField(max_length=264,null=True)
    def __str__(self):
        return self.ac_name
        return self.ac_post
        return self.ac_number
# class EC_Post(models.Model):
#     name = models.ForeignKey('Executive_Counsil',
#     on_delete=models.CASCADE)
#     ec_post = models.CharField(max_length=264,unique=True)
#     def __str__(self):
#         return self.ec_post
# class EC_Number(models.Model):
    
#     post = models.ForeignKey('EC_Post',
#     on_delete=models.CASCADE)
#     ec_number = models.CharField(max_length=264,unique=True)
#     def __str__(self):
#         return self.ec_number 
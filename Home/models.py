from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from  django.utils import timezone
class Catalogy(models.Model):
    nameCatalog = models.CharField("Loại công việc",max_length=50)
    
    def __str__(self):
        return self.nameCatalog
    
    def get_absolute_url(self):
        return reverse ('category', args=(str(self.id)))

class Post(models.Model):
    nameJob = models.CharField("Tên công việc",max_length=100)
    catalogy = models.ForeignKey(Catalogy, on_delete=models.CASCADE, default=0)
    nhatuyen = models.ForeignKey(User, on_delete=models.CASCADE)
    motacv = models.TextField("Mô Tả công việc")
    phucloi = models.TextField("Phúc lợi")
    yeucaucv = models.TextField("Yêu cầu conog việc")
    salary = models.CharField("Lương",max_length=50)
    diachi = models.CharField("Địa chỉ",max_length=50)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField("Hình ảnh",null= True, blank=True, upload_to="images/")
    care = models.ManyToManyField(User, related_name='posts')

    def total_care(self):
        return self.care.count()

    def __str__(self):
        return self.nameJob

    def get_absolute_url(self):
        return reverse ('post_details', args=(str(self.id)))
        #return reverse ('/')

class Post_cv(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Họ và tên",max_length=100)
    email = models.CharField("Địa chỉ email",max_length=100)
    cv_file = models.FileField("Chọn CV File",null=True, blank=True, upload_to="CV_File/")

    def __str__(self):
        return self.post_id.nameJob


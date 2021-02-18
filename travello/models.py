from django.db import models

# Create your models here.
class destination(models.Model):
    
    name = models.CharField(max_length=20)
    description = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class watches(models.Model):
        description = models.TextField()
        price = models.IntegerField()
        img = models.ImageField(upload_to='pics')
        brand = models.CharField(max_length=20,default='benson')
        offer = models.BooleanField(default=False)
        @staticmethod
        def get_watch(ids):
         return watches.objects.filter(id__in = ids)
    


class cloth(models.Model):
    genderno = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    brand = models.CharField(max_length=20,default='khadi')
    sale = models.BooleanField(default=False)
    @staticmethod
    def get_cloths(ids):
      return cloth.objects.filter(id__in = ids)
    

class shoes(models.Model):
    genderno = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    brand = models.CharField(max_length=20,default='J.')
    sale = models.BooleanField(default=False)
    @staticmethod
    def get_product(ids):
      return shoes.objects.filter(id__in = ids)
    
class perfumes(models.Model):
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    brand = models.CharField(max_length=20,default='Dior')
    offer = models.BooleanField(default=False)
    @staticmethod
    def get_product_by_id(ids):
      return perfumes.objects.filter(id__in = ids)
        #a={}
        #i=0
        #for ids in ids:
          #a[i]= perfumes.objects.filter(id=ids)
          #i = i+1

class popular(models.Model):
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    @staticmethod
    def get_popular(ids):
      return popular.objects.filter(id__in = ids)

class recommend(models.Model):
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    
    
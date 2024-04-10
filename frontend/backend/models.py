from django.db import models

class movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_date = models.CharField(max_length=10)
    movie_image = models.ImageField(default='default')
    movie_runtime = models.TimeField(default='00')
    movie_director = models.CharField(max_length=50)
    movie_description = models.TextField(max_length=1500)
    movie_genre = models.CharField(max_length=20) 

    def __str__(self):
        return self.movie_name
    
class vehicles(models.Model):
    name = models.CharField(max_length=50)
    veh_image1 = models.ImageField(default='default')
    veh_image2 = models.ImageField(default='default')
    veh_image3 = models.ImageField(default='default')
    veh_image4 = models.ImageField(default='default')
    veh_image5 = models.ImageField(default='default')
    veh_type = models.CharField(max_length=20)
    veh_price = models.BigIntegerField()
    veh_company = models.CharField(max_length=20)
    veh_desc = models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class gaming(models.Model):
    game_name = models.CharField(max_length=50)
    game_image1 = models.ImageField(default='default')
    game_image2 = models.ImageField(default='default')
    game_image3 = models.ImageField(default='default')
    game_image4 = models.ImageField(default='default')
    game_image4 = models.ImageField(default='default')
    game_Genre = models.CharField(max_length=20)
    game_size = models.CharField(max_length=20)
    game_reqm = models.TextField(max_length=1500)
    game_desc = models.CharField(max_length=1500)
    game_platform = models.CharField(default='null',max_length=100)
    
    def __str__(self):
        return self.game_name

class electronics(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_image1 = models.ImageField(default="default")
    pro_image2 = models.ImageField(default="default")
    pro_image3 = models.ImageField(default="default")
    pro_image4 = models.ImageField(default="default")
    pro_image5 = models.ImageField(default="default")
    pro_desc = models.TextField(max_length=1500)
    pro_price = models.CharField(max_length=10)
    pro_release = models.CharField(max_length=10)
    pro_type = models.CharField(max_length=10)
    pro_company = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.pro_name
    
class products(models.Model):
    Prod_name = models.CharField(max_length=20)
    prod_rel = models.CharField(max_length=20)
    prod_desc = models.TextField(max_length=1500)
    prod_company = models.CharField(max_length=25)
    prod_price = models.CharField(max_length=20)
    prod_type = models.CharField(max_length=25)
    prod_image = models.ImageField(default='default')
    prod_genre = models.CharField(max_length=20)
    prod_platform = models.CharField(max_length=20)
    prod_reqm = models.CharField(max_length=100)
    prod_director = models.CharField(max_length=100)
    pro_runtime = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Prod_name
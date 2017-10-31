from django.db import models

# Create your models here.
class Level1(models.Model):
    pass

class Level2(models.Model):
    l1 = models.ForeignKey(Level1)
    def __str__(self): return "%s, %s"%(self.id, self.l1.id)

class Level3(models.Model):
    l2 = models.ForeignKey(Level2)


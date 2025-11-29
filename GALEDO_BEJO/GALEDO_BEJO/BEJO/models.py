from django.db import models

# Create your models here.

class parentClass(models.Model):
    name = models.CharField(max_length=200)
    parent = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}{self.parent}'
    
class childClass (models.Model):
    nameParent = models.ForeignKey(parentClass, on_delete=models.DO_NOTHING, )
    nameChild = models.CharField(max_length=200)
    relationshipData = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nameParent}{self.relationshipData}'
    
class schoolClass(models.Model):
    nameChild = models.ForeignKey(childClass, on_delete=models.DO_NOTHING)
    school = models.CharField(max_length=200)
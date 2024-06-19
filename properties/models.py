from django.db import models


# Create your models here.
class properties(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location_id = models.CharField()
    image_url = models.ImageField()
    property_type = models.CharField()
    service_type = models.CharField()
    agent_id = models.IntegerField()
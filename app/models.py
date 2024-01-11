from django.db import models
from datetime import datetime
# Create your models here.
class m_model(models.Model):
    name = models.CharField( max_length=50)
    auto_field = models.AutoField(primary_key=True)
    birthday = models.DateTimeField()
    email = models.EmailField(max_length=254 )
    file = models.FileField(upload_to='files/' ,default=None)
    boolean_field = models.BooleanField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    float_field = models.FloatField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    time_field = models.TimeField()
    url_field = models.URLField()


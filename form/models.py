from django.db import models

# Create your models here.
class M_form(models.Model):
    model_name = 'form'

    ID_TYPE_CHOICES = (
        ('CC', 'Cedula'),
        ('ID', 'Id'),
    )

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_type = models.CharField(max_length=2, choices=ID_TYPE_CHOICES)
    id_number = models.CharField(max_length=10)
    credit_value = models.IntegerField()
    interest = models.FloatField()
    months = models.IntegerField()
    adviser = models.CharField()
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'form'

    def __str__(self):
        return self.name
    
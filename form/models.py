from django.db import models

# Create your models here.
class M_form(models.Model):
    model_name = 'form'

    ID_TYPE_CHOICES = (
        ('CC', 'Cedula'),
        ('ID', 'Id'),
    )

    name = models.CharField(null=False, blank=False,max_length=35)
    last_name = models.CharField(null=False, blank=False,max_length=35)
    id_type = models.CharField(null=False, blank=False, choices=ID_TYPE_CHOICES)
    id_number = models.IntegerField(null=False, blank=False,max_length=10, unique=True)
    credit_value = models.IntegerField(null=False, blank=False)
    interest = models.FloatField(null=False, blank=False)
    months = models.IntegerField(null=False, blank=False)
    adviser = models.CharField(null=False, blank=False, max_length=35)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'form'

    def __str__(self):
        return self.name
    
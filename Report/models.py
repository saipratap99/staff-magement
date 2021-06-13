from django.db import models

# Create your models here.
class Staff(models.Model):
  staff_id = models.BigAutoField(primary_key=True)
  staff_name = models.CharField(max_length=100)
  designation = models.CharField(max_length=100)
  salary = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.staff_name

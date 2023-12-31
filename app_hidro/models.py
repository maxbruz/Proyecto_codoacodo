from django.db import models

class Producto (models.Model):
    class Meta:
        db_table= "lista_productos"

    IDp=models.IntegerField(blank=False,null=False, primary_key=True)
    Descrip=models.CharField(max_length=200)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Obs=models.CharField(max_length=200)
    Stock=models.FloatField(blank=True,null=False)
    Sold=models.FloatField(blank=True,null=False)
    URLimg=models.CharField(max_length=200)


    def __str__(self):
        return f"El producto: {self.Descrip} codigo {self.IDp} con Stock de {self.Stock}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
             for field in self.__class__._meta.fields[1:]
        ]


from django.db import models

# Create your models here.

class Lista(models.Model):
    """Model definition for Lista."""
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=10)
    nameid = models.CharField(max_length=40)

    class Meta:
        """Meta definition for Listák."""

        verbose_name = 'Lista'
        verbose_name_plural = 'Lista'

    def __str__(self):
        return f"{self.name} - {self.amount} - (id : {self.nameid})"

    def create(json):
        query = Lista.objects.filter(nameid=json['id'])
        if not list(query):
            try:
                Lista(nameid=json["id"], name=json["nev"], amount = json["mennyiseg"]).save()
                return {'response': True, 'massage': "Sikeresen hozzáadva"}
            except ValueError:
                return {'response': ValueError, 'massage': ValueError}
        else:
            return {'response': 'nemjó', 'massage': 'Már van meglévő'}
    def delete(json):
        query = Lista.objects.filter(nameid=json['id'])
        if not list(query):
            return 'nem talált item'
        else:
            try:
                query.delete()
                return True
            except ValueError:
                return ValueError

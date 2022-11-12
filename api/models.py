from django.db import models

class medicament(models.Model):
    id = models.AutoField(primary_key=True)
    nom  = models.CharField(max_length=64)
    groupeMed = models.ForeignKey("groupeMedicament",on_delete=models.PROTECT)
    prix_de_vente = models.IntegerField()


    def __str__(self):
        return f"{self.nom} de {self.prix_de_vente}FBu"

class groupeMedicament(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.TextField()

    def __str__(self):
       return self.nom 



class Achat(models.Model):
	id = models.BigAutoField(primary_key=True)
	medicament = models.ForeignKey(medicament, on_delete=models.PROTECT)
	quantite = models.IntegerField()
	prix_total = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	expire_date = models.DateField()

	def __str__(self):
		return f"{self.quantite} {self.medicament.nom}s coutant {self.prix_total}FBu"

class stock(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.IntegerField()









class Vente(models.Model):
	id = models.BigAutoField(primary_key=True)
	medicament = models.ForeignKey(medicament, on_delete=models.PROTECT)
	quantite = models.IntegerField()
	prix = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	

	def __str__(self):
		return f"{self.quantite} {self.medicament.nom} à {self.prix_total}FBu"


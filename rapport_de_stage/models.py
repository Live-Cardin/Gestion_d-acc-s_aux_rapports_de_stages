from django.db import models
from django.contrib.auth.models import User

class Departement(models.Model):
    nom=models.CharField(max_length=60)
    faculte=models.CharField(max_length=60)
    option=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
class Personnel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    niveau=models.CharField(max_length=50,null=True)
    tel=models.IntegerField(null=True)
    


class Rapport(models.Model):
    sujet=models.CharField( max_length=200)
    rapport_pdf=models.FileField(upload_to='media/')
    departement=models.ForeignKey("Departement" , on_delete=models.PROTECT,null=True)
    personnel=models.ForeignKey("Personnel",on_delete=models.PROTECT)
    date_defendu=models.DateTimeField()

    def __str__(self):
        return self.sujet

 
 
class Etudiant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    departement=models.ForeignKey("Departement", on_delete=models.PROTECT,null=True)
    tel=models.IntegerField(null=True)


    def __str__(self):
        return self.prenom

    
    
class Consultant(models.Model):
    etudiant=models.ForeignKey("Etudiant", on_delete=models.PROTECT)
    rapport=models.ForeignKey("Rapport",on_delete=models.PROTECT)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
     


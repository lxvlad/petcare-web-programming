
from django.conf import settings
from django.db import models
class Pet(models.Model):
    SPECIES_CHOICES=[("dog","Dog"),("cat","Cat"),("other","Other")]
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="pets")
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=10,choices=SPECIES_CHOICES,default="dog")
    breed=models.CharField(max_length=100,blank=True)
    sex=models.CharField(max_length=10,choices=[("male","Male"),("female","Female")],default="male")
    birth_date=models.DateField(null=True,blank=True)
    weight_kg=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    photo_url=models.URLField(blank=True)
    def __str__(self): return f"{self.name} ({self.species})"
class Vaccination(models.Model):
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,related_name="vaccinations")
    name=models.CharField(max_length=100)
    date=models.DateField()
    next_due=models.DateField(null=True,blank=True)
    vet_clinic=models.CharField(max_length=200,blank=True)
class Appointment(models.Model):
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,related_name="appointments")
    date=models.DateTimeField()
    type=models.CharField(max_length=100)
    notes=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=[("planned","planned"),("done","done"),("canceled","canceled")],default="planned")
class Note(models.Model):
    KIND_CHOICES=[("feeding","feeding"),("medicine","medicine"),("walk","walk"),("custom","custom")]
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,related_name="notes")
    date=models.DateTimeField(auto_now_add=True)
    kind=models.CharField(max_length=20,choices=KIND_CHOICES,default="custom")
    text=models.TextField(blank=True)

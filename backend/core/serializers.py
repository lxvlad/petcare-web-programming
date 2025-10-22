
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet,Vaccination,Appointment,Note
class UserSerializer(serializers.ModelSerializer):
    class Meta: model=User; fields=["id","username","email"]
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta: model=User; fields=["username","email","password"]
    def create(self,validated_data): return User.objects.create_user(**validated_data)
class PetSerializer(serializers.ModelSerializer):
    class Meta: model=Pet; fields="__all__"
class VaccinationSerializer(serializers.ModelSerializer):
    class Meta: model=Vaccination; fields="__all__"
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta: model=Appointment; fields="__all__"
class NoteSerializer(serializers.ModelSerializer):
    class Meta: model=Note; fields="__all__"

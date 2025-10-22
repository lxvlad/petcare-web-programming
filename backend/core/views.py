
from rest_framework import viewsets,permissions,generics
from django.contrib.auth.models import User
from .models import Pet,Vaccination,Appointment,Note
from .serializers import RegisterSerializer,PetSerializer,VaccinationSerializer,AppointmentSerializer,NoteSerializer
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]
class PetViewSet(viewsets.ModelViewSet):
    serializer_class=PetSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        qs=Pet.objects.all()
        owner=self.request.query_params.get("owner")
        return qs.filter(owner_id=owner) if owner else qs
class VaccinationViewSet(viewsets.ModelViewSet):
    serializer_class=VaccinationSerializer
    def get_queryset(self):
        qs=Vaccination.objects.all()
        pet=self.kwargs.get("pet_id") or self.request.query_params.get("pet")
        return qs.filter(pet_id=pet) if pet else qs
class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class=AppointmentSerializer
    def get_queryset(self):
        qs=Appointment.objects.all()
        pet=self.kwargs.get("pet_id") or self.request.query_params.get("pet")
        return qs.filter(pet_id=pet) if pet else qs
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    def get_queryset(self):
        qs=Note.objects.all()
        pet=self.kwargs.get("pet_id") or self.request.query_params.get("pet")
        return qs.filter(pet_id=pet) if pet else qs

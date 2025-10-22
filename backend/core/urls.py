
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterView,PetViewSet,VaccinationViewSet,AppointmentViewSet,NoteViewSet
router=DefaultRouter()
router.register(r"pets",PetViewSet,basename="pets")
router.register(r"vaccinations",VaccinationViewSet,basename="vaccinations")
router.register(r"appointments",AppointmentViewSet,basename="appointments")
router.register(r"notes",NoteViewSet,basename="notes")
urlpatterns=[ path("auth/register/",RegisterView.as_view(),name="register"), path("",include(router.urls)) ]

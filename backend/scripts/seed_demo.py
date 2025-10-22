import datetime
from django.contrib.auth.models import User
from core.models import Pet, Vaccination, Appointment, Note

def ensure_user():
    u, created = User.objects.get_or_create(username="demo", defaults={"email":"demo@example.com"})
    if created or not u.has_usable_password():
        u.set_password("demo12345")
        u.save()
    return u

def run():
    u = ensure_user()

    dog, _ = Pet.objects.get_or_create(owner=u, name="Buddy", defaults=dict(
        species="dog", breed="Labrador", sex="male", birth_date=datetime.date(2021,5,15),
        weight_kg=24.5, photo_url="/media/pets/dog_1.jpg"
    ))
    cat, _ = Pet.objects.get_or_create(owner=u, name="Misty", defaults=dict(
        species="cat", breed="British Shorthair", sex="female", birth_date=datetime.date(2022,3,12),
        weight_kg=4.3, photo_url="/media/pets/cat_1.jpg"
    ))

    Vaccination.objects.get_or_create(pet=dog, name="Rabies", date=datetime.date(2025,5,10),
                                      defaults=dict(next_due=datetime.date(2026,5,10), vet_clinic="VetCare Lviv"))
    Vaccination.objects.get_or_create(pet=cat, name="FVRCP", date=datetime.date(2025,6,1),
                                      defaults=dict(next_due=datetime.date(2026,6,1), vet_clinic="Cat Clinic"))

    Appointment.objects.get_or_create(pet=dog, date=datetime.datetime(2025,11,1,10,30), type="checkup",
                                      defaults=dict(notes="Annual check", status="planned"))
    Appointment.objects.get_or_create(pet=cat, date=datetime.datetime(2025,12,12,9,0), type="grooming",
                                      defaults=dict(notes="Nail trim", status="planned"))

    Note.objects.get_or_create(pet=dog, kind="feeding", text="Dry food 150g")
    Note.objects.get_or_create(pet=cat, kind="medicine", text="1/2 tablet after dinner")
    print("✅ Seeded demo data. Login: demo / demo12345")

from django.urls import path

from .views import (
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingByPatientAndDeleteView,
)

urlpatterns = [
    path("", PatientDoctorMappingListCreateView.as_view(), name="mapping-list-create"),
    path(
        "<int:pk>/",
        PatientDoctorMappingByPatientAndDeleteView.as_view(),
        name="mapping-by-patient-delete",
    ),
]
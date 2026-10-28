

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from patients.models import Patient
from .models import Doctor, PatientDoctorMapping
from .serializers import DoctorSerializer
from .mapping_serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related("patient", "doctor")

    def perform_create(self, serializer):
        patient = serializer.validated_data["patient"]

        if patient.created_by != self.request.user:
            raise PermissionDenied(
                "You can only assign doctors to your own patients."
            )

        serializer.save()


class PatientDoctorMappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient_id=self.kwargs["patient_id"],
            patient__created_by=self.request.user,
        ).select_related("patient", "doctor")





class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]




class PatientDoctorMappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )


class PatientDoctorMappingByPatientAndDeleteView(generics.GenericAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related("patient", "doctor")

    def get(self, request, pk):
        mappings = self.get_queryset().filter(patient_id=pk)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = self.get_queryset().filter(id=pk).first()

        if mapping is None:
            from rest_framework.exceptions import NotFound
            raise NotFound("Mapping not found.")

        mapping.delete()
        return Response(status=204)
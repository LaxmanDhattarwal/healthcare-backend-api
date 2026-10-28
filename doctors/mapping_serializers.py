
from rest_framework import serializers

from patients.models import Patient
from .models import Doctor, PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient", "doctor", "assigned_at"]
        read_only_fields = ["id", "assigned_at"]

    def validate(self, attrs):
        request = self.context.get("request")
        patient = attrs.get("patient")
        doctor = attrs.get("doctor")

        if request and patient and patient.created_by != request.user:
            raise serializers.ValidationError({
                "patient": "You can only assign doctors to your own patients."
            })

        if patient and doctor:
            exists = PatientDoctorMapping.objects.filter(
                patient=patient,
                doctor=doctor,
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "This doctor is already assigned to this patient."
                )

        return attrs

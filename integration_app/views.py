from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def student_summary(request, student_id):
    student = requests.get(f"http://localhost:8000/api/students/{student_id}/").json()
    library = requests.get(f"http://localhost:8000/api/library/{student_id}/").json()
    payments = requests.get(f"http://localhost:8000/api/payments/{student_id}/").json()

    return Response({
        "student": student,
        "library_status": library,
        "payments": payments
    })

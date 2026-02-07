from django.shortcuts import render
from rest_framework.decorators import api_view
from library_app.models import LibraryRecord
from rest_framework.response import Response

@api_view(['GET'])
def getLIbraryRecords(request, student_id):
    records = LibraryRecord.objects.filter(student_id=student_id).first()
    if not records:
        return Response({
            'student_id': student_id,
            'has_fines': False,
            'amount_due': 0.0,
        })
    return Response({
        'student_id': records.student_id,
        'has_fines': records.has_fines,
        'amount_due': records.amount_due,
    })
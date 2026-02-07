from django.urls import path
from .views import getLIbraryRecords

urlpatterns = [
    path('api/library/<str:student_id>/', getLIbraryRecords),
]
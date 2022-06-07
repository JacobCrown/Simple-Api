from django.views.generic.list import ListView
from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentListView(ListView):
    model = Student
    queryset = Student.objects.all()
    context_object_name = 'student_list'
    template_name = 'api/student_list.html'

class StudentNameListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    model = Student

    def get_queryset(self):
        return Student.objects.filter(imie=self.kwargs['name'])


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'


class StudentDestroyAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

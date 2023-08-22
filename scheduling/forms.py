from django import forms
from .models import Course, Lecture

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'

from django.contrib import admin
from .models import Instructor, Course, Lecture

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Lecture)

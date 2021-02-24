from django.contrib import admin
from .models import Course, Course_group, Student, Ranking

admin.site.register(Course)
admin.site.register(Course_group)
admin.site.register(Student)
admin.site.register(Ranking)

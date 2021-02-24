from rest_framework import serializers
from .models import Course, Course_group, Student, Ranking


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'Semester', 'lecturer', 'capacity', 'day', 'time_start', 'time_end']


class Course_groupSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Course_group
        fields = ['id', 'name', 'courses']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'user', 'amount_elective']


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ['id', 'rank', 'student', 'course_group']

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Course_group, Student, Ranking
from .serializers import CourseSerializer, Course_groupSerializer, StudentSerializer, RankingSerializer


class Course_groupViewSet(viewsets.ModelViewSet):
    queryset = Course_group.objects.all()
    serializer_class = Course_groupSerializer

    @action(detail=False, methods=['GET'])
    def get_last_rating(self, request):
        # user = request.user
        ranking = Ranking.objects.filter(student=1).order_by('rank')
        if len(ranking) == 0:  # the user not rank his courses
            print("rank=0")
            courses = Course_group.objects.all()
            serializer = Course_groupSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:  # the user rank his courses, show his last rank
            print("rank!=0")
            courses = []
            for rank in ranking:
                courses.append(Course_group.objects.get(name=rank.course_group.name))
            serializer = Course_groupSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False, methods=['GET'])
    def get_semester_a(self, request):
        courses = Course.objects.filter(Semester="א")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_semester_b(self, request):
        courses = Course.objects.filter(Semester="ב")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_semester_s(self, request):
        courses = Course.objects.filter(Semester="ק")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer

    @action(detail=False, methods=['POST'])
    def rank_courses(self, request):
        # user = request.user
        is_rated = Ranking.objects.filter(student=1).order_by('rank')
        ranking = request.data['ranks']
        if len(is_rated) == 0:  # the user not rank his courses (create)
            for index, movie_rank in enumerate(ranking):
                course = Course_group.objects.get(name=movie_rank['name'])
                student = Student.objects.get(user=1)
                Ranking.objects.create(course_group=course, student=student, rank=index+1)
            return Response('Ranking created', status=status.HTTP_200_OK)
        else:  # the user rank his courses (update)
            for index, movie_rank in enumerate(ranking):
                last_rank = Ranking.objects.get(course_group=movie_rank['id'], student=1)
                last_rank.rank = index+1
                last_rank.save()
            return Response('Ranking updated', status=status.HTTP_200_OK)
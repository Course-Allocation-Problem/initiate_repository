from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CourseViewSet, Course_groupViewSet, StudentViewSet, RankingViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('course_group', Course_groupViewSet)
router.register('student', StudentViewSet)
router.register('ranking', RankingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

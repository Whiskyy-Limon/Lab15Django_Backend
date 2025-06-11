from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, SerieViewSet, CategoriaViewSet


router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'series', SerieViewSet)
router.register(r'categories', CategoriaViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice, Serie, Categoria
from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer,
    SerieSerializer, CategoriaSerializer
)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        quiz = self.get_object()
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        results = []
        for answer in serializer.validated_data:
            try:
                question = Question.objects.get(id=answer['question_id'], quiz=quiz)
                choice = Choice.objects.get(id=answer['choice_id'], question=question)
                results.append({
                    'question_id': question.id,
                    'correct': choice.is_correct
                })
            except:
                results.append({
                    'question_id': answer['question_id'],
                    'error': 'Invalid question or choice'
                })

        correct = sum(1 for r in results if r.get('correct'))
        return Response({
            'score': f"{correct}/{len(results)}",
            'results': results
        })

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        return QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
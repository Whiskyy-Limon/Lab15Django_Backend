from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Categoria(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Serie(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.DateField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
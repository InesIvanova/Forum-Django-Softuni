from django.db import models

# Create your models here.


class Question(models.Model):
    author = models.CharField(max_length=200)
    question = models.TextField()

    def __str__(self):
        return f'Question from {self.author} - {self.question[:20]}'


class Forreasens(models.Model):
    name = models.CharField(max_length=200)


class Answer(models.Model):
    author = models.CharField(max_length=200, default='Anonymos')
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    name = models.ForeignKey(Forreasens, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Answer from {self.author}'

from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phaseNum = models.IntegerField()

    def __str__(self):
        return self.name


class question(models.Model):
    questionText = models.CharField(max_length=100)
    correctAnswer = models.TextField()

    def __str__(self):
        return self.questionText


class answeredQuestion(models.Model):
    uid = models.ForeignKey('user')
    qid = models.ForeignKey('question')
    userAnswer = models.TextField()
    questionPassed = models.BooleanField()

    def __str__(self):
        return self.uid+" "+self.qid+" "+self.userAnswer

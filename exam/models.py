from django.db import models


class QuestionnaireModel(models.Model):

    question = models.TextField(max_length=200)
    a = models.TextField(max_length=50)
    b = models.TextField(max_length=50)
    c = models.TextField(max_length=50)
    d = models.TextField(max_length=50)

    

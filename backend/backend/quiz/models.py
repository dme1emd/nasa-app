from django.db import models
# Create your models here.
class Question(models.Model) : 
    choices = (
        (1,1),
        (2,2) ,
        (3,3) ,
    )
    text = models.CharField(max_length=100)
    right_answer = models.OneToOneField('Answer' , on_delete=models.CASCADE)
    wrong_answer_one = models.OneToOneField('Answer' , on_delete=models.CASCADE , related_name='quest')
    wrong_answer_two = models.OneToOneField('Answer' , on_delete=models.CASCADE , related_name='questi' , default =None)
    difficulty = models.PositiveSmallIntegerField(choices=choices)
    pic = models.ImageField(upload_to = 'question_pics')
    def __str__(self):
        return self.text
class Answer(models.Model) : 
    text = models.CharField(max_length=30)
    def __str__(self):
        return self.text
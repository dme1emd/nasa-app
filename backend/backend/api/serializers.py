from django.db import models
from rest_framework import serializers
from profiles.models import Profile
from quiz.models import Answer ,Question
from mars.models import Moon , Mars
# Create your models here.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Profile
        fields = ['id' , 'unique_key' , 'username' , 'email' , 'profile_pic' , 'points']
class AnswerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Answer
        fields = ['text' , 'id']
class QuizSerializer(serializers.ModelSerializer) : 
    right_answer = AnswerSerializer()
    wrong_answer_one = AnswerSerializer()
    wrong_answer_two = AnswerSerializer()
    class Meta :
        model = Question
        fields = '__all__'
class MoonSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Moon
        fields = '__all__'
class MarsSerializer(serializers.ModelSerializer):
    moons = MoonSerializer(many = True)
    class Meta : 
        model = Mars
        fields = '__all__'
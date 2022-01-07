from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from RestApi import models
from RestApi.models import User,Attempts,Answers,Question,Choices


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = "__all__"

class QuestionsSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id','name', 'section','choose','text', 'choices']

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields=("question","AttemptId","other")

class AnswersSerializerString(serializers.ModelSerializer):
    question = serializers.StringRelatedField(many=False)
    choice =  serializers.StringRelatedField(many=False)
    other = serializers.StringRelatedField(many=False)

    class Meta:
        model = Answers
        fields=("question","choice","other")

class AttemptSerializer(serializers.ModelSerializer):
    answers=AnswersSerializerString(many=True,read_only=True)
    class Meta:
        model = Attempts
        fields=("answers","started_at")
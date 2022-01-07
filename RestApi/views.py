from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from RestApi.models import  Question,Attempts
from RestApi.serializers import QuestionsSerializer,AnswersSerializer,AttemptSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getQuestions(request,section):
    questions =Question.objects.all().filter(section=section)
    response = QuestionsSerializer(instance=questions, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def Answer(request):
    serializer = AnswersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['user']=request.user
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Answer added successfully "
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAttempts(request):
    attempts =Attempts.objects.all().filter(user=request.user)
    response = AttemptSerializer(instance=attempts, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)
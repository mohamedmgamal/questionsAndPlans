from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .serializer import RegisterSerializer

@api_view(['POST'])
def signUp(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "New user added successfully "
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
# from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


# Create your views here.
class MemberList(APIView):
    #this get method returns all members, it's used for testing
    def get(self, request):
        members = models.Member.objects.all()
        serializer = serializers.MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommitteeList(APIView):
    #this get method returns all committees, it's used for testing
    def get(self, request):
        committees = models.Committee.objects.all()
        serializer = serializers.CommitteeSerializer(committees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CommitteeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Member.objects.get(pk=pk)
        except models.Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = serializers.MemberSerializer(member)
        return Response(serializer.data)


class CommitteeDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Committee.objects.get(pk=pk)
        except models.Committee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        committee = self.get_object(pk)
        serializer = serializers.CommitteeSerializer(committee)
        return Response(serializer.data)

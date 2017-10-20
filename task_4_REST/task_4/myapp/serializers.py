from rest_framework import serializers
from . import models


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Committee
        fields = '__all__'

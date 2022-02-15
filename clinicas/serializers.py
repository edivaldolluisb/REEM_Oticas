from rest_framework import serializers
from .models import Agendamento, Encomenda


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class EncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encomenda
        fields = '__all__'



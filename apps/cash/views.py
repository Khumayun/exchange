from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import ExchangeSerializer
from .models import Exchange


def index(request):
    return render(request, 'apps/index.html', {})


class ExchangeCreateView(CreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

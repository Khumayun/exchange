from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializers import ExchangeSerializer
from .models import Exchange
from .forms import *

def index(request):
    return render(request, 'apps/index.html', {})

class ExchangeCreateView(ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

def posterview(request):
	template_name = 'test.html'
	myform =  Myform(request.POST or None)
	context = {
		'myform': myform
	}
	return render(request, template_name, context)
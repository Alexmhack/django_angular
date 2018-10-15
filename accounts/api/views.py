from rest_framework import generics

from .serializers import AccountSerializer
from accounts.models import Account

class AccountListAPIView(generics.ListCreateAPIView):
	serializer_class = AccountSerializer
	queryset = Account.objects.all()

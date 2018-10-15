from rest_framework import serializers

from leads.models import Lead

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lead
		fields = "__all__"

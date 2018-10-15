from rest_framework import serializers

from opportunities.models import Opportunity

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Opportunity
		fields = "__all__"

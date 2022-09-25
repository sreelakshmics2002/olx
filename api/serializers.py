from rest_framework import serializers
from api.models import VehicleReviews,Vehicles
from django.contrib.auth.models import User

class VehicleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    model = serializers.CharField()
    color = serializers.CharField()
    price =serializers.IntegerField()
    transmission = serializers.CharField()

    def create(self, validated_data):
        return Vehicles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.model = validated_data.get("model")
        instance.color = validated_data.get("color")
        instance.price = validated_data.get("price")
        instance.transmission = validated_data.get("transmission")

    # # FIELD LEVEL VALIDATION
    # def validate_price(self, value):
    #     if value not in range(50, 1000):
    #         raise serializers.ValidationError("invalid price")
    #     return value
    #
    # def validate_qty(self, value):
    #     if value not in range(1, 500):
    #         raise serializers.ValidationError("invalid quantity")
    #     return value

    # OBJECT LEVEL VALIDATION BY OVERRIDING VALIDATE METHOD
    # def validate(self,data):
    #     price=data.get("price")
    #     qty=data.get("qty")
    #     if qty not in range(1,500):
    #         raise serializers.ValidationError("invalid quantity")
    #     if price not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return data


class VehicleReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.CharField(read_only=True)

    class Meta:
        model = VehicleReviews
        fields = "__all__"
        # exclude=("created_date",)





class VehicleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
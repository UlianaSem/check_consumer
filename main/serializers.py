from rest_framework import serializers

from main import models


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = [
            'id',
            'place_id',
            'place_name',
        ]


class PlaceSerializer(serializers.ModelSerializer):
    taxes_amount = serializers.SerializerMethodField()
    category_analytics = serializers.SerializerMethodField()

    class Meta:
        model = models.Place
        fields = [
            'place_id',
            'place_name',
            'total_purchases',
            'average_receipt',
            'taxes_amount',
            'category_analytics',
        ]

    @staticmethod
    def get_taxes_amount(instance):
        return {
            "total_nds": instance.total_nds,
            "total_tips": instance.total_tips
        }

    @staticmethod
    def get_category_analytics(instance):
        result = {}
        for category in instance.categories.all():
            result[category.name] = {
                "total_spent": category.total_spent,
                "average_receipt": category.average_receipt
            }

        return result

from decimal import Decimal

from main import models


def calculate_categories(price, category, place):
    place = models.Place.objects.get(place_id=place)

    if not models.Category.objects.filter(place=place).filter(name=category).exists():
        models.Category.objects.create(
            name=category,
            total_spent=price,
            average_receipt=price,
            place=place,
        )
    else:
        cat_obj = models.Category.objects.filter(place=place).filter(name=category).first()

        cat_obj.total_spent += Decimal(price)
        cat_obj.average_receipt = (cat_obj.average_receipt + Decimal(price)) / 2

        cat_obj.save()


def calculate_places(total_amount, nds_amount, tips_amount, place_id, place_name):
    if not models.Place.objects.filter(place_id=place_id).exists():
        models.Place.objects.create(
            place_id=place_id,
            place_name=place_name,
            total_purchases=1,
            average_receipt=total_amount,
            total_nds=nds_amount,
            total_tips=tips_amount,
        )
    else:
        place_obj = models.Place.objects.get(place_id=place_id)

        place_obj.total_purchases += 1
        place_obj.average_receipt = (place_obj.average_receipt + Decimal(total_amount)) / 2
        place_obj.total_nds += Decimal(nds_amount)
        place_obj.total_tips += Decimal(tips_amount)

        place_obj.save()

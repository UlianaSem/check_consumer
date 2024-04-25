from celery import shared_task

from main import models, services


@shared_task
def calculate_analytics():
    checks = models.Check.objects.filter(is_calculated=False)

    for check in checks:
        place = check.check_json.get('place')

        if place is not None:
            total_amount = check.check_json.get('total_amount')
            nds_amount = check.check_json.get('nds_amount')
            tips_amount = check.check_json.get('tips_amount')
            place_id = place.get('place_id')
            place_name = place.get('place_name')
            services.calculate_places(
                total_amount,
                nds_amount,
                tips_amount,
                place_id,
                place_name,
            )

            items = check.check_json.get('items')

            for item in items:
                category = item.get('category')
                price = item.get('price')
                services.calculate_categories(price=price, category=category, place=place_id)

        check.is_calculated = True
        check.save()

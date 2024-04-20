import json

from django.db import migrations
import pandas as pd


def load_data_from_excel(apps, schema_editor):
    # Load data from excel
    df = pd.read_excel("DB_음식_20230715.xlsx")

    food_instances = []
    Food = apps.get_model("mysite", "Food")

    for index, row in df.iterrows():
        food_instance = Food(
            food_id=row['SAMPLE_ID'],
            food_cd=row['식품코드'],
            group_name=row['DB군'],
            food_name=row['식품명'],
            research_year=row['연도'],
            market_name=row['지역 / 제조사'],
            ref_name=row['채취시기'],
            serving_size=row['1회제공량'],
            calorie = row["에너지(㎉)"],
            carbohydrate = row["수분(g)"],
            protein = row["단백질(g)"],
            province = row["지방(g)"],
            sugars = row["총당류(g)"],
            salt = row["나트륨(㎎)"],
            cholesterol = row["콜레스테롤(㎎)"],
            saturated_fatty_acis = row["총 포화 지방산(g)"],
            trans_fat = row["트랜스 지방산(g)"],
        )
        food_instances.append(food_instance)

    Food.objects.bulk_create(food_instances)


class Migration(migrations.Migration):
    dependencies = [
        (
            "platform",
            "0006_alter_food_group_name.py",
        ),
    ]

    operations = [
        migrations.RunPython(
            load_data_from_excel, reverse_code=migrations.RunPython.noop
        ),
    ]

import json

from django.db import migrations
import pandas as pd


def load_data_from_excel(apps, schema_editor):
    # Load data from excel
    df = pd.read_excel("mysite/food/migrations/DB_음식_20230715.xlsx")
    food_instances = []
    Food = apps.get_model("food", "Food")


    for index, row in df[:100].iterrows():
        food_instance = Food(
            food_id=row['SAMPLE_ID'],
            food_cd=row['식품코드'],
            group_name=row['DB군'],
            food_name=row['식품명'],
            research_year=row['연도'],
            market_name=row['지역 / 제조사'],
            ref_name=row['채취시기'],
            serving_size= row['1회제공량'] if isinstance(row["1회제공량"], int) else None,
            calorie = float(row["에너지(㎉)"]) if is_num(row["에너지(㎉)"])  else None,
            carbohydrate = float(row["수분(g)"]) if is_num(row["수분(g)"]) else None,
            protein = float(row["단백질(g)"]) if is_num(row["단백질(g)"]) else None,
            province = float(row["지방(g)"]) if is_num(row["지방(g)"]) else None,
            sugars = float(row["총당류(g)"]) if is_num(row["총당류(g)"]) else None,
            salt = float(row["나트륨(㎎)"]) if is_num(row["나트륨(㎎)"]) else None,
            cholesterol = float(row["콜레스테롤(㎎)"]) if is_num(row["콜레스테롤(㎎)"]) else None,
            saturated_fatty_acids = float(row["총 포화 지방산(g)"]) if is_num(row["총 포화 지방산(g)"])else None,
            trans_fat = float(row["트랜스 지방산(g)"]) if is_num(row["트랜스 지방산(g)"]) else None,
        )
        food_instances.append(food_instance)

    Food.objects.bulk_create(food_instances)

def is_num(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class Migration(migrations.Migration):
    dependencies = [
        (
            "food",
            "0006_alter_food_group_name",
        ),
    ]

    operations = [
        migrations.RunPython(
            load_data_from_excel, reverse_code=migrations.RunPython.noop
        ),
    ]

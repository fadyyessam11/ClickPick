# Generated by Django 4.1.9 on 2023-07-01 22:59

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('Marketplace', models.CharField(max_length=255)),
                ('ProductTitle', models.CharField(max_length=255)),
                ('ProductBrand', models.CharField(max_length=255)),
                ('ProductCategory', models.CharField(max_length=255)),
                ('ProductDescription', models.TextField()),
                ('ProductID', models.CharField(max_length=255)),
                ('ProductImage', models.URLField()),
                ('ProductLink', models.URLField()),
                ('ProductOffer', models.CharField(max_length=255)),
                ('ProductOldPrice', models.CharField(max_length=255)),
                ('ProductPrice', models.CharField(max_length=255)),
                ('ProductRatingCount', models.CharField(max_length=255)),
                ('ProductRatings', models.CharField(max_length=255)),
                ('ProductReviews', models.CharField(max_length=255)),
                ('ProductSpecifications', models.CharField(max_length=255)),
                ('ProductSubCategory', models.CharField(max_length=255)),
                ('SellerID', models.CharField(max_length=255)),
                ('SellerName', models.CharField(max_length=255)),
                ('SellerUrl', models.URLField()),
                ('ProductMatchingIDs', models.CharField(max_length=255)),
                ('ProductSentimentReviews', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Products_Test_Collection',
                'managed': False,
            },
        ),
    ]

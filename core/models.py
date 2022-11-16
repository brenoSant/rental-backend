from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        managed = True
        abstract = True


class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=40,
        unique=True,
        null=False
    )

    class Meta:
        db_table = 'employee'


class Customer(ModelBase):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    class MaritalStatus(models.TextChoices):
        SINGLE = 'S', 'Single'
        MARRIED = 'M', 'Married'
        DIVORCED = 'D', 'Divorced'
        WIDOWER = 'W', 'Widower'

    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=40
    )
    gender = models.CharField(
        db_column='tx_gender',
        null=False,
        max_length=1,
        choices=Gender.choices
    )
    marital_status = models.CharField(
        db_column='tx_marital_status',
        null=False,
        max_length=1,
        choices=MaritalStatus.choices
    )
    email = models.CharField(
        db_column='tx_email',
        null=False,
        max_length=256
    )

    class Meta:
        db_table = 'customer'


class Rental(ModelBase):
    customer = models.ForeignKey(
        db_column='id_customer',
        null=False,
        to='Customer',
        on_delete=models.DO_NOTHING
    )
    employee = models.ForeignKey(
        db_column='id_employee',
        null=False,
        to='Employee',
        on_delete=models.DO_NOTHING
    )
    expected_delivery_date = models.DateField(
        db_column='dt_expected_delivery_date',
        null=False
    )
    delivery_date = models.DateField(
        db_column='dt_delivery_date',
        null=True
    )

    class Meta:
        db_table = 'rental'


class Category(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=40
    )

    class Meta:
        db_table = 'category'


class Dvd(ModelBase):
    category = models.ForeignKey(
        db_column='id_category',
        on_delete=models.DO_NOTHING,
        to='Category',
        null=False
    )

    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=40
    )
    price = models.DecimalField(
        db_column='nb_price',
        max_digits=10,
        decimal_places=2,
        null=False
    )

    class Meta:
        db_table = 'dvd'


class RentalItem(ModelBase):
    rental = models.ForeignKey(
        db_column='id_rental',
        null=False,
        on_delete=models.DO_NOTHING,
        to='Rental'
    )
    dvd = models.ForeignKey(
        db_column='id_dvd',
        null=False,
        on_delete=models.DO_NOTHING,
        to='Dvd'
    )
    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False
    )
    price = models.DecimalField(
        db_column='nb_price',
        max_digits=10,
        decimal_places=2,
        null=False
    )

    class Meta:
        db_table = 'rental_item'

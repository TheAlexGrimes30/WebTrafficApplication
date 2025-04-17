from django.core.validators import MinValueValidator
from django.db import models

class Status(models.Model):
    status_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class TransactionType(models.Model):
    type_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    type_model = models.ForeignKey(TransactionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        db_table = "subcategories"
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

class DDSRecord(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type_model = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    sum_amount = models.IntegerField(validators=[MinValueValidator(1)])
    comment = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"record_{self.pk}"

    class Meta:
        db_table = "records"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

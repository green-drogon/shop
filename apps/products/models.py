from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="نام دسته‌بندی"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="دسته‌بندی",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام محصول",
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="اسلاگ",
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    price = models.PositiveBigIntegerField(
    verbose_name="قیمت (تومان)"
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="موجودی",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول",
    )

    image = models.ImageField(
        upload_to="products/",
        verbose_name="تصویر",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.product.name} Image"
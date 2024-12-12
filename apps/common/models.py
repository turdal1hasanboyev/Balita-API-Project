from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Makes the model abstract (no database table will be created for this model)
        verbose_name = "Base Model"  # Singular name for the model
        verbose_name_plural = "Base Models"  # Plural name for the model


class Subscribe(BaseModel):
    email = models.EmailField(max_length=100, db_index=True, unique=True)
    url = models.URLField(max_length=150, db_index=True, unique=True)

    class Meta:
        verbose_name = "Subscribe"
        verbose_name_plural = "Subscribes"
    
    def __str__(self):
        return f"{self.email}-{self.url}"

"""Blog/abstract_models."""
from django.db import models

CHAR_PER_MESSAGE = 20


class BaseModel(models.Model):
    """BaseModel"""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    def __str__(self):
        return self.title[:CHAR_PER_MESSAGE]

    class Meta:
        abstract = True
        ordering = ('created_at',)

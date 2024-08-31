"""Blog/utils."""
from django.utils.timezone import now


def get_filtered_qs(queryset, **kwargs):

    filters = {
        'is_published': True,
        'pub_date__lt': now(),
        'category__is_published': True,
        **kwargs,
    }
    return queryset.select_related(
        'author', 'category', 'location').filter(**filters)
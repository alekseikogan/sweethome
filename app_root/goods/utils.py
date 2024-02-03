from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank, SearchHeadline)
from goods.models import Product


def q_search(query):
    '''Поиск по ключевым словам'''

    # Поиск по id
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    result = Product.objects.annotate(
        rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    result = result.annotate(
        headline=SearchHeadline(
            'name',
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel='</span>'
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            'description',
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel='</span>'
        )
    )

    return result

    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # # Поиск по названию и описанию
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Product.objects.filter(q_objects)
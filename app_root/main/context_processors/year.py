import datetime as dt


def year(request):
    '''Определяет текущий год'''
    return {
        'year': dt.datetime.today().year
    }

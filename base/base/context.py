# base/rstsite_context.py

from django.conf      import settings

from rstblog.models import Article
from rstblog.models import Category
from rstblog.const  import TYPES



def siteconf(request):
    '''site configuration params availabe to templates'''
    return {
        'ABSTRACT': settings.SITE.get('ABSTRACT', ''),
        'WTITLE': settings.SITE.get('WTITLE', ''),
        'WSUBTITLE': settings.SITE.get('WSUBTITLE', ''),
        'WLICENSE': settings.SITE.get('WLICENSE', ''),
        'WLICENSEREF': settings.SITE.get('WLICENSEREF', ''),
    }
    
def used_categories(request):
    '''categories used in every atype
    
    return: a dictionary, keys are atypes, values are 
            lists of used categories in that atype
    '''
    
    used_cats = {}
    all_cats = Category.objects.all()
    atypes = list(TYPES.keys())

    for atype in atypes:
        cats = [
            category.name
            for category in all_cats
            if Article.objects.filter(category=category, atype=atype).count()
            > 0
        ]
        used_cats[atype] = cats.copy()
    return {'categories': used_cats.copy()}
    



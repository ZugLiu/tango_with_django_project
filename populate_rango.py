# if we just want to change values in a database, we don't neet to migrate. Just re-run the script!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries contaning the pages we want to add into each category
    # The we will create a dictionary of dictionaries for our categories.
    # It allows us to iterate through each data structure, and add the data to our models

    python_pages = [
         {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views':12},
         {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views':15},
         {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views':34}
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views':20},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views':13},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views':54}
    ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views':22},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views':21}
    ]

    cats = {'Python':{'pages':python_pages, 'views':128, 'likes':64},
            'Django':{'pages':django_pages, 'views':64, 'likes':32},
            'Other Frameworks':{'pages':other_pages, 'views':32, 'likes':16}
    }

    # The code below goes through the cats dictionary, then adds each category, and then adds all the associated pages for that category
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
        
            
    
    # print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):  # create a model instance with a specified name by Category.objects.get_or_create(name=name)[0]. set other attributes to a speficied value
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
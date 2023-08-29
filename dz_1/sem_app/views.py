from django.shortcuts import render
from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Hello world')
    return HttpResponse("Привет мир!")


def head(request):
    today = datetime.datetime.today().date()
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           '<head>' \
           '<meta charset="UTF-8">' \
           '<title>Главная</title>' \
           '</head>' \
           '<body>' \
           '<h1>Главная</h1>' \
           '<p>Первый Django сайт</p>' \
           f'<p>Сегодня: {today} </p>' \
           '</body>' \
           '</html>'
    return HttpResponse(html)


def about_me(request):
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           '<head>' \
           '<meta charset="UTF-8">' \
           '<title>О себе</title>' \
           '</head>' \
           '<body>' \
           '<h1>О себе</h1>' \
           '<p>Меня зовут Елена</p>' \
           '<p>Я из города Киров</p>' \
           '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Map_of_Russia_-_Kirov_Oblast_%28Crimea_disputed%29.svg/800px-Map_of_Russia_-_Kirov_Oblast_%28Crimea_disputed%29.svg.png">'\
           '</body>' \
           '</html>'
    return HttpResponse(html)

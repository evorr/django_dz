from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging


logger = logging.getLogger(__name__)


def coin(request):
    words = ['Орел', 'Решка']
    result = words[randint(0, 1)]
    logger.info(result)
    return HttpResponse(f'{result}')


def cube(request):
    result = randint(1, 6)
    logger.info(result)
    return HttpResponse(f'{result}')


def rnd100(request):
    result = randint(1, 100)
    logger.info(result)
    return HttpResponse(f'{result}')




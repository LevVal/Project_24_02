from django.http import HttpResponse

from django.views import View
import random

class ToDoView(View):
    def get(self, request, *args, **kwargs):
        to_do = ''
        deal = ['<li>Поспать</li>',
                 '<li>Поесть</li>',
                 '<li>Почистить зубы</li>',
                 '<li>Потанцевать</li>',
                 '<li>Поработать</li>']

        for i_deal in range(5):
            to_do += deal[random.randint(0, 4)]

        return HttpResponse('<ul>' + to_do + '</ul>')

from django.urls import path

from catalog.views import home, contacts, category_list

urlpatterns = [
    path('', home, name='home'),
    path('category/', category_list , name='categories'),
    path('contacts/', contacts, name='contacts')
]
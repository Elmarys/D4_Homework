from django.urls import path
from .views import NewsList, NewsSearch, NewsDetail, NewsCreate, NewsDelete, NewsEdit

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('search/', NewsSearch.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('add/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
]
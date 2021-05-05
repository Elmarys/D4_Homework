from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются(

obscene_words = [
    'Путин',
]

@register.filter(name='censor') # регестрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def censor(value): # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргуменит — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    for word in obscene_words:
        if word in value:
            new_value = value.replace(word, "***")
            return new_value
        else:
            return value
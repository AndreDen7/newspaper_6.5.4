from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError(f'Тип данных{type(value)} нельзя проверить на цензуру')
    list_censor = [
        'хуй', 'хуи', 'хуя', 'бля', 'бляд', 'пизд', 'ебан', 'ебаны', 'сука',
    ]
    for word in list_censor:
        check = (value.lower()).find(word)
        while check != -1:
            len_ = len(word)
            value = value[:check] + '*' * len_ + value[check + len_:]
            check = (value.lower()).find(word)
    return value


@register.filter(name='is_filters_uses')
def is_filters_uses(value):
    filters_arg = value.find('&')
    if filters_arg != -1:
        is_first_list_now = value.find('?')
        if value[(is_first_list_now + 1): (is_first_list_now + 5)] == 'page':
            return value[filters_arg:]
        else:
            return ('&' + value[is_first_list_now + 1:])
    else:
        return ''

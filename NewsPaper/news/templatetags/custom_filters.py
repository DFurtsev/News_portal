from django import template

register = template.Library()


@register.filter()
def censor(value):
    bad_words = ['козявка', 'негодяй', 'подлец', 'засранец']
    moder_text = value
    for i in value.split():
        if i.lower() in bad_words:
            print(len(i))
            word = i[0] + '*' * (len(i) - 1)
            moder_text = moder_text.replace(i, word)
    return moder_text

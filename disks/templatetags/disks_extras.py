from django import template
register = template.Library()

@register.filter(is_Safe=True)
def duration(milliseconds):
    t = milliseconds/1000
    m = t//60
    s = t%60
    return "%02d:%02d" %(m, s)

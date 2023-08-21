from django import template
register = template.Library()


# views.py
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    
    return value.split(key) 

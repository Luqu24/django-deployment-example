from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    """
    THIS CUT OUT ALL THE VALUES OF "arg" FROM THE STRING
    """

    return value.replace(arg,"")

# register.filter('cut',cut)

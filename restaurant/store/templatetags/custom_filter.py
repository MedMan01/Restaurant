from django import template

register = template.Library()# permet d'enregistrer les filtres personnalisés et de les rendre disponibles dans les templates.

@register.filter(name='currency')
def currency(number):
    return str(number)+"DH"



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1


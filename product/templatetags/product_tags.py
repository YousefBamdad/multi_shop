from django import template

register = template.Library()


@register.simple_tag
def call_sell_price(price, discount):
    if discount is None or discount is 0:
        return price
    sell_price = int(price - (price * discount / 100))
    return sell_price

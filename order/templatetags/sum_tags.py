# 템플릿에서 파이썬으로 넘겨 처리하고 다시 템플릿으로 넘김
# 서버레벨에서 하는게 아닌 프론트레벨에서 처리함
# 많이 쓰면 느려짐
from django import template

register = template.Library()

@register.simple_tag
def sum_prices(object_list):
    return sum(item.total_price for item in object_list)
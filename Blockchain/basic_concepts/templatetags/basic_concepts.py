from django import template
import hashlib
from django.utils.html import mark_safe
register = template.Library()

@register.filter
def sha256(content):
    h = hashlib.new('sha256')
    h.update(bytes(content,'utf-8'))
    # hexadecimal
    hash_value = h.hexdigest()
    
    if content == '':
        hash_value = ''
    return hash_value

@register.simple_tag
def join_and_hash(arg1, arg2):

    joined = str(arg1) + str(arg2)

    h = hashlib.new('sha256')
    h.update(bytes(joined,'utf-8'))
    hash_value = h.hexdigest()

    if joined == '':
        hash_value = ''
    return hash_value 

@register.simple_tag
def top_hash(arg1, arg2, arg3, arg4):
    
    joined12 = str(arg1) + str(arg2)

    h12 = hashlib.new('sha256')
    h12.update(bytes(joined12,'utf-8'))
    hash_value_12 = h12.hexdigest()

    joined34 = str(arg3) + str(arg4)

    h34 = hashlib.new('sha256')
    h34.update(bytes(joined34,'utf-8'))
    hash_value_34 = h34.hexdigest()

    joined1234 = str(hash_value_12) + str(hash_value_34)
    h1234 = hashlib.new('sha256')
    h1234.update(bytes(joined1234,'utf-8'))
    hash_value_1234 = h1234.hexdigest()

    if str(arg1) + str(arg2) + str(arg3) + str(arg4) == '':
        hash_value_1234 = ''
    return hash_value_1234

import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    new_order_id = random_string_generator().upper()
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=new_order_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_order_id


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    print(slug, "this is your slug you printing")
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        randstr = random_string_generator(size=4)
        print(randstr, "ben your randon string")
        slug=slug
        print(slug,'Your second slug again')
        new_slug= f'{slug}-{randstr}'
        print(new_slug, "your new slug")
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


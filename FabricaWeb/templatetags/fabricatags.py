
from django import template
from accounts.models import User

register = template.Library()

@register.simple_tag(takes_context = True)
def is_authenticated(context):
    request = context['request']
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])
            return True
        except User.DoesNotExist:
            return False
    else:
        return False


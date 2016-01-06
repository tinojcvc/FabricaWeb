
from django import template
from accounts.models import User

register = template.Library()

@register.assignment_tag(takes_context=True)
def is_authenticated(context):
    """
    Este tag retorna True si es user_id valido y lo asigna a la variable
    is_logged del template base.html para despues cargar los menus
    """
    request = context['request']
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])
            if user:
                return True
            else:
                return False
        except User.DoesNotExist:
            return False
    else:
        return False

@register.assignment_tag(takes_context=True)
def is_user_admin(context):
    request = context['request']
    if 'user_id' in request.COOKIES:
        try:
            user = User.objects.get(id=request.COOKIES['user_id'])
            return user.is_admin
        except User.DoesNotExist:
            return False
    else:
        return False


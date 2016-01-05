from functools import wraps
from django.utils.decorators import available_attrs
from django.http import HttpResponseRedirect

from accounts.models import User

def user_test(login_url=None):
    """
    Ayuda a verificar que el usuario este logeado, si no lo esta
    lo redirecciona a la pagina de login
    """
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if 'user_id' in request.COOKIES:
                try:
                    user = User.objects.get(id=request.COOKIES['user_id'])
                    if user:
                        return view_func(request, *args, **kwargs)
                except User.DoesNotExist:
                    return HttpResponseRedirect(login_url)
            else:
                return HttpResponseRedirect(login_url)
        return _wrapped_view
    return decorator


def login_required(function=None):
    """
    Decorador para las vistas, verifica que el usuario este logeado
    """
    actual_decorator = user_test(login_url = '/accounts/sigin/')
    if function:
        return actual_decorator(function)
    return actual_decorator


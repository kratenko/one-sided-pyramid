from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home',)
def my_view(request):
    return Response("This pyramid has only one side.")

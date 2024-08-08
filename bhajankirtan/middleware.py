from django.http import HttpResponseForbidden


class RestrictDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_domain = '0.0.0.0:3000'

        origin = request.headers.get('Origin') or request.headers.get('Referer')

        if origin and allowed_domain not in origin:
            return HttpResponseForbidden('Access denied.')

        response = self.get_response(request)
        return response

from django.shortcuts import redirect # pour rediriger l'utilisateur vers une autre URL.

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):# Cette fonction sera appelée pour chaque demande entrante.
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']# récupère l'URL actuelle à partir du dictionnaire request.META qui est valeur de PATH_INFO
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware
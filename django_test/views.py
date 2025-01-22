from django.http import HttpResponse


def home(request):
    return HttpResponse(
        """
        <html>
        <head>
            <title>Welcome to Django</title>
        </head>
        <body>
            <h1>Congratulations!</h1>
            <p>You’ve successfully created a Django project.</p>
        </body>
        </html>
        """
    )

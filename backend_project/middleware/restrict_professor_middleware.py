from django.http import JsonResponse

class ProfessorOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith("/api/assignment/"):
            if not request.user.is_authenticated or not request.user.is_staff:
                return JsonResponse(
                    {"detail": "Only professors can manage assignments"},
                    status=403
                )

        return self.get_response(request)

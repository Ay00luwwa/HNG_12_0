from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    data = {
        "email": "ijidakinroayooluwa@gmail.com", 
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Ay00luwwa/HNG_12_0/"
    }
    return JsonResponse(data)
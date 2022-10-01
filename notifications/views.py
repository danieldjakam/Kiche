from django.shortcuts import render

# Create your views here.
def all_notifications(req):
    return render(req, 'pages/list_notifications.html', {})
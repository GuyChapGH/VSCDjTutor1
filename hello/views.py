import re
from django.utils.timezone import datetime
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    
    print("http://127.0.0.1:8000/hello/VSCode")
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %Y at %X")

# Filter the nam arguments to letters only using regular expressions. URL arguments
# can contain arbitary text, so we restrict to safe characters only.

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
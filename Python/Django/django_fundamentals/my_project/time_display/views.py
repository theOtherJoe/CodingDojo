from django.shortcuts import render
from datetime import datetime
import pytz
from pytz import timezone
from time import localtime, strftime
    
def index(request):
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    context = {
        "time": date.strftime("%b %d, %Y %I:%M %p")
    }
    return render(request,'index.html', context)
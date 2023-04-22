from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse

import logging
import os
logger = logging.getLogger('mylogger')

def index(request):  
#   logger.info("start index func ,request=" + str(request))
    return HttpResponse("Hello Django!!!")

def index(request):
    return render(
        request,
        'drtsai/index.html',
        # 'drtsai/top-nav-sidebar.html',
    #     {
    #         # 'name': name,
    #         'date': datetime.now() 
    #     }
    )

def his(request, name):
    # return HttpResponse(name)
    # return render(request, 'drtsai/404.html')    
    return render(
        request,
        'drtsai/hismain.html',
        {
            'name': name,
            'date': datetime.now() 
        }
    )
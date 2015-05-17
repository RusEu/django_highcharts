from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from visitor.visitor_utils import *
from django.contrib.gis.geoip import GeoIP
from visitor.models import Visitor

def index(request):
	return render_to_response("index.html")
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from visitor.visitor_utils import *
from django.contrib.gis.geoip import GeoIP
from visitor.models import Visitor
from django import template

def index(request):
	tmp_country = {}
	for item in Visitor.objects.all():
		if item.country in tmp_country:
			tmp_country[str(item.country)] += 1
		else:
			tmp_country[str(item.country)] = 1
	val = 0
	for item , value in tmp_country.items() :
		val = val + value
	percent = 100 / val
	countrylist={}
	for item , value in tmp_country.items():
		countrylist[str(item)] = value * percent
	return render_to_response("index.html",{"countrylist":countrylist})
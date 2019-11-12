# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import ClusterForm

import os

# Create your views here.
def home2(request):

    tmp = [list(filter(lambda k: 'v2' != k, i.split('_'))) for i in results_name] 
    form = ClusterForm()
    return render(request, 'cluster_form.html', {'form': form})

def home(request):
    results_tar = os.listdir('/var/www/html/cmc_models/')
    results_name = [i.split('.tar.')[0] for i in results_tar]
    results = zip(results_tar,results_name)
    return render(request, 'index.html', {'results' : results})

def index(request):
    return redirect('/home')

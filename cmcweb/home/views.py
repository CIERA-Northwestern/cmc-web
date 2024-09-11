# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import ClusterForm

import os

# Create your views here.
def home(request):
    form = ClusterForm()
    return render(request, 'cluster_form.html', {'form': form})

def index(request):
    return redirect('/home')

def download_cluster(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = ClusterForm(request.GET)
        # check whether it's valid:

        if form.is_valid():
            number_of_objects = form.cleaned_data['number_of_objects']
            virial_radius = form.cleaned_data['virial_radius']
            galactocentric_distance = form.cleaned_data['galactocentric_distance']
            metallicity = form.cleaned_data['metallicity']
            filename = '{0}_{1}_{2}_{3}.tar.gz'.format(number_of_objects,virial_radius,galactocentric_distance,metallicity)
            return redirect('/cmc-models/{0}'.format(filename))
        else:
            return render(request, 'cluster_form.html', {'form': form})

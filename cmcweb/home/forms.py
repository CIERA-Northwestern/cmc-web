from django import forms
import os
import numpy

results_tar = os.listdir('/var/www/html/cmc_models/')
results_name = [i.split('.tar.')[0] for i in results_tar]
tmp = [list(filter(lambda k: 'v2' != k, i.split('_'))) for i in results_name]
number_of_objects = numpy.unique(numpy.array(tmp)[:,0])
virial_radius = numpy.unique(numpy.array(tmp)[:,1])
galactocentric_distance = numpy.unique(numpy.array(tmp)[:,2])
metallicity = numpy.unique(numpy.array(tmp)[:,3])

class ClusterForm(forms.Form):
    #number_of_objects = forms.CharField(label='How many initial objects are in the GC')
    number_of_objects = forms.ChoiceField(choices=tuple(zip(number_of_objects,number_of_objects)))
    #virial_radius = forms.CharField(label='This is the Virial Radius of the GC')
    virial_radius = forms.ChoiceField(choices=tuple(zip(virial_radius, virial_radius)))
    #galactocentric_distance = forms.CharField(label='This is the radial position in the Galaxy')
    galactocentric_distance = forms.ChoiceField(choices=tuple(zip(galactocentric_distance, galactocentric_distance)))
    #metallicity = forms.CharField(label='Metallicity of the GC')
    metallicity = forms.ChoiceField(choices=tuple(zip(metallicity, metallicity)))

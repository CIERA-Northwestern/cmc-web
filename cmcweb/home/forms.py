from django import forms
  

class ClusterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ClusterForm, self).__init__(*args, **kwargs)
        self.NOBJECTS_CHOICES = kwargs.pop('NOBJECTS_CHOICES', ((None, None)))
        self.VIRIAL_RADIUS_CHOICES = kwargs.pop('VIRIAL_RADIUS_CHOICES', ((None, None)))
        self.GALACTOCENTRIC_CHOICES = kwargs.pop('GALACTOCENTRIC_CHOICES', ((None, None)))
        self.METALLICITY_CHOICES = kwargs.pop('METALLICITY_CHOICES', ((None, None)))
        #number_of_objects = forms.CharField(label='How many initial objects are in the GC')
        number_of_objects = forms.ChoiceField(choices=self.NOBJECTS_CHOICES,)
        #virial_radius = forms.CharField(label='This is the Virial Radius of the GC')
        virial_radius = forms.ChoiceField(choices=self.VIRIAL_RADIUS_CHOICES,)
        #galactocentric_distance = forms.CharField(label='This is the radial position in the Galaxy')
        galactocentric_distance = forms.ChoiceField(choices=self.GALACTOCENTRIC_CHOICES,)
        #metallicity = forms.CharField(label='Metallicity of the GC')
        metallicity = forms.ChoiceField(choices=self.METALLICITY_CHOICES,)

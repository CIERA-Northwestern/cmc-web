# ClusterMonteCarlo (CMC) Web
This repository host the Django source code used to produce cluster webserver: http://cmc.ciera.northwestern.edu/

# requirements
```
conda create -n django-cmc -c conda-forge python=3.7 django psycopg2 django-crispy-forms sqlparse
```

# environmental variable requirements
Please add the following to your `~/.bash_profile`
```
export CMC_NAME=
export CMC_USER=
export CMC_PASSWORD=
export CMC_HOST=
export CMC_PORT=
```
Contact Scott Coughlin https://ciera.northwestern.edu/directory/scott-coughlin/
for this information.

# Run local development server
cd cmcweb
python manage.py runserver

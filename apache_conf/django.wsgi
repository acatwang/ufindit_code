import os
import sys


#p = '/var/www/html/ufindit_code/django_app'
#sys.path.append(p)

#if p not in sys.path:
#    sys.path.append(p)
#    sys.path.append(p+"/django_app")
#    sys.path.append(p + "/django_app/qac")
#    sys.path.append('/var/www/html')

# Activate your virtual env
root = os.path.join(os.path.dirname(__file__),'..')
sys.path.insert(0,root)
sys.path.insert(0,"/var/www/html/ufindit_code/django_app")

packages = os.path.join(root,'/qac/env/lib/python2.7/site-packages')
sys.path.insert(0,packages)
#site.addsitedir(packages)


activate_env=os.path.join(root,
                          '../ufindit_code/django_app/qac/env/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

for p in sys.path:
    print >> sys.stderr, p

os.environ['DJANGO_SETTINGS_MODULE'] = 'qac.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

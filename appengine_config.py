from google.appengine.ext import vendor
import os, sys

on_appengine = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
if on_appengine and os.name == 'nt':
    sys.platform = "Not Windows"

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
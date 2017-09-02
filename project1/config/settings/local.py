from .base import *

with open(os.path.join(BASE_DIR, "config", "settings", "local.json")) as f:
    local = json.load(f)

DEBUG = True
SECRET_KEY = local['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': local['ENGINE'],
        'NAME': local['NAME'],
        'USER': local['USER'],
        'PASSWORD': local['PASSWORD'],
    }
}

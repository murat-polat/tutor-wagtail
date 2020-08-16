from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "add": {
        "SECRET_KEY": "{{ 24|random_string }}",
    },
# Django application need this configurations
# After installation of plugin, run:
# "tutor config save --set wagtail_HOST=wagtail.{{LMS_HOST}}" and the others
    "defaults": {
        "HOST": "wagtail.{{ LMS_HOST }}",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/wagtail",
        "MYSQL_HOST": "mysql",
        "MYSQL_PORT": 3306,
        "MYSQL_DATABASE": "wagtail",
        "MYSQL_USERNAME": "wagtail",
        "MYSQL_PASSWORD": "wagtail"
    }

}

hooks = {
# Pull and build docker containers
    "build-image": {"wagtail": "muratp/wagtail"},
    "remote-image": {"wagtail": "muratp/wagtail"},
# Initial all services
    "init": ["mysql","lms","wagtail"]
}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches

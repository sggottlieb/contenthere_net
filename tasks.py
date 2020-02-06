# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file
from pathlib import PurePath
from slugify import slugify
from jinja2 import Template



SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Port for `serve`
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    c.run('pelican -s {settings_base}'.format(**CONFIG))

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican -d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican -r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))

@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def publish(c):
    """Publish to production via rsync"""
    
    
    c.run(f"aws s3 sync {SETTINGS['OUTPUT_PATH']} s3://{SETTINGS['S3_BUCKET']} --acl public-read --delete")
    
@task
def newpost(c, title, tags):
    MD_TEMPLATE = \
"""Title: {{title.replace("\n", " ")}}
Date: {{publish_date}}
Modified: {{update_date}}
Category: misc
Tags: {{tag_str}}
Slug: {{path}}.html
Authors: Seth Gottlieb

"""


    dt = datetime.datetime.now()
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    day = dt.strftime("%d")

    context = {}
    context["title"] = title
    context["tag_str"] = tags
    context["publish_date"] = context["update_date"] = dt.isoformat()
    path = context["path"] = PurePath(year, month, slugify(title))
    filepath = str(PurePath("content", path)) + ".md"
    print(filepath)

    template = Template(MD_TEMPLATE)
    content = template.render(**context)
    print(content)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as f:
        f.write(template.render(**context))





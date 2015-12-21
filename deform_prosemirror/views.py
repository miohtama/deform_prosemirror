from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_deform import CSRFSchema

import deform
import colander

from .widget import ProseMirrorWidget


DEFAULT_TEXT="""
# Welcome to ProseMirror demo

This is a [ProseMirror](http://prosemirror.net) test widget.

## Instructions

* Edit this text

* Press save

* See reflected Markdown results
"""


def get_widget_js_tags(request, form):
    """Generate JS and CSS tags for a widget.

    For demo purposes only - you might have something specific to your application here.

    See http://docs.pylonsproject.org/projects/deform/en/latest/widget.html#the-high-level-deform-field-get-widget-resources-method
    """
    resources = form.get_widget_resources()
    js_resources = resources['js']
    js_links = [ request.static_url(r) for r in js_resources ]
    js_tags = ['<script type="text/javascript" src="%s"></script>' % link for link in js_links]
    return js_tags


def get_widget_css_tags(request, form):
    """Generate JS and CSS tags for a widget.

    For demo purposes only - you might have something specific to your application here.

    See http://docs.pylonsproject.org/projects/deform/en/latest/widget.html#the-high-level-deform-field-get-widget-resources-method
    """
    resources = form.get_widget_resources()
    css_resources = resources['css']
    css_links = [ request.static_url(r) for r in css_resources ]
    css_tags = ['<link rel="stylesheet" href="%s"/>' % link for link in css_links]
    return css_tags

class MySchema(CSRFSchema):
    """Username-less registration form schema."""

    test_text = colander.SchemaNode(
        colander.String(),
        title='ProseMirror demo widget',
        default=DEFAULT_TEXT,
        widget=ProseMirrorWidget())



@view_config(route_name='home', renderer='templates/home.pt')
def home(request):

    schema = MySchema().bind(request=request)

    # Manage <head> JS and CSS for Deform widgets
    resource_registry = deform.widget.ResourceRegistry()

    form = deform.Form(schema, buttons=('submit', ), resource_registry=resource_registry)

    reflected_markdown = None
    rendered_form = None

    if 'submit' in request.POST:

        controls = request.POST.items()

        try:
            appstruct = form.validate(controls)
            reflected_markdown = appstruct["test_text"]
        except deform.ValidationFailure as e:
            rendered_form = e.render()

    rendered_form = rendered_form or form.render()

    widget_js_tags = get_widget_js_tags(request, form)
    widget_css_tags = get_widget_css_tags(request, form)

    return locals()


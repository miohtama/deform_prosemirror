from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_deform import CSRFSchema

import deform
import colander

from .widget import ProseMirrorWidget
from .widget import get_widget_resource_tags


class MySchema(CSRFSchema):
    """Username-less registration form schema."""

    test = colander.SchemaNode(
        colander.String(),
        title='Test test',
        widget=ProseMirrorWidget())



@view_config(route_name='home', renderer='templates/home.pt')
def home(request):

    schema = MySchema().bind(request=request)

    resource_registry = deform.widget.ResourceRegistry()
    form = deform.Form(schema, buttons=('submit', ), resource_registry=resource_registry)

    if 'submit' in request.POST:

        controls = request.POST.items()

        try:
            appstruct = form.validate(controls)

            return HTTPFound(request.route_url("home"))

        except deform.ValidationFailure as e:
            rendered_form = e.render()
    else:
        rendered_form = form.render()

    widget_tags = get_widget_resource_tags(request, form)

    return locals()


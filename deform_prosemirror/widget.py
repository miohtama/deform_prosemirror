from deform import widget


class ProseMirrorWidget(widget.TextInputWidget):
    readonly_template = 'readonly/richtext'
    delayed_load = False
    strip = True
    template = 'deform_prosemirror/prosemirror'
    requirements = ( ('prosemirror', None), )


def get_widget_resource_tags(request, form):
    """Generate JS and CSS tags for a widget.

    For demo purposes only - you might have something specific to your application here.

    See http://docs.pylonsproject.org/projects/deform/en/latest/widget.html#the-high-level-deform-field-get-widget-resources-method
    """
    resources = form.get_widget_resources()
    js_resources = resources['js']
    css_resources = resources['css']
    js_links = [ request.static_url(r) for r in js_resources ]
    css_links = [ request.static_url(r) for r in css_resources ]
    js_tags = ['<script type="text/javascript" src="%s"></script>' % link for link in js_links]
    css_tags = ['<link rel="stylesheet" href="%s"/>' % link for link in css_links]
    tags = js_tags + css_tags
    return tags
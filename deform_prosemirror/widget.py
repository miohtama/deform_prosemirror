from deform import widget


class ProseMirrorWidget(widget.TextInputWidget):
    readonly_template = 'readonly/richtext'
    delayed_load = False
    strip = True
    template = 'deform_prosemirror/prosemirror'
    requirements = ( ('prosemirror', None), )


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
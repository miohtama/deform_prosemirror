import json

from deform import widget


class ProseMirrorWidget(widget.TextInputWidget):
    readonly_template = 'readonly/richtext'
    delayed_load = False
    strip = True
    template = 'deform_prosemirror/prosemirror'
    requirements = ( ('prosemirror', None), )

    prosemirror_options = {
      "docFormat": "markdown",
      "tooltipMenu": False,
      "menuBar": True,
    }

    def get_prosemirror_options_as_json(self):
        return json.dumps(self.prosemirror_options)



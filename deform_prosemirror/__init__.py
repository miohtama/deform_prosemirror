from pyramid.config import Configurator
from pyramid_deform import configure_zpt_renderer



def includeme(config):
    config.add_static_view('prosemirror-static', 'deform_prosemirror:static/')
    configure_zpt_renderer(["deform_prosemirror:templates"])

    # Include our JS in the default Deform resource registry
    from deform.widget import default_resources

    default_resources.update({
        "prosemirror": {
            None: {
                "js": "deform_prosemirror:static/prosemirror-bundle.js"
            }
        }
    })


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    from pyramid.session import UnencryptedCookieSessionFactoryConfig
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(settings=settings, session_factory=my_session_factory)

    config.include('pyramid_chameleon')
    config.include('pyramid_deform')
    config.include('deform_prosemirror')

    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()

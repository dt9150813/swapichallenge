# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557103777.492711
_enable_loop = True
_template_filename = 'C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['tag', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def tag():
            return render_tag(context._locals(__M_locals))
        films = context.get('films', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tag'):
            context['self'].tag(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tag(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tag():
            return render_tag(context)
        __M_writer = context.writer()
        __M_writer('Movie List')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        films = context.get('films', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <!-- ##### Breadcumb Area Start ##### -->\r\n    <div class="breadcumb_area bg-img" style="background-image: url(')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/img/bg-img/breadcumb.jpg);">\r\n        <div class="container h-100">\r\n            <div class="row h-100 align-items-center">\r\n                <div class="col-12">\r\n                    <div class="page-title text-center">\r\n                        <h2>Movie List</h2>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <!-- ##### Breadcumb Area End ##### -->\r\n\r\n    <!-- ##### Shop Grid Area Start ##### -->\r\n    <section class="shop_grid_area section-padding-80">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-12 col-md-12 col-lg-12">\r\n                    <table class="table table-borderless sortable">\r\n                            <thead>\r\n                                <tr>\r\n                                    <th class="text-center"><h4>Film Poster</h4></th>\r\n                                    <th class="text-center"><h4>Film Name</h4></th>\r\n                                    <th class="text-center"><h4>Episode #</h4></th>\r\n                                    <th class="text-center"><h4>Released Date</h4></th>\r\n                                </tr>\r\n                            </thead>\r\n                            <tbody>\r\n')
        for film in films:
            __M_writer('                                <tr>\r\n                                    <td class="text-center"><a href="/homepage/film/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[3]))
            __M_writer('"><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[7]))
            __M_writer('" style="max-width: 120px;"></a></td>\r\n                                    <td class="text-center" style="vertical-align:middle"><a href="/homepage/film/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[3]))
            __M_writer('"><h5>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[0]))
            __M_writer('</h5></a></td>\r\n                                    <td class="text-center" style="vertical-align:middle"><h5>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[1]))
            __M_writer('</h5></td>\r\n                                    <td class="text-center" style="vertical-align:middle"><h5>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[2]))
            __M_writer('</h5></td>\r\n                                </tr>\r\n')
        __M_writer('                            </tbody>\r\n                    </table>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </section>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 2, "51": 47, "57": 2, "63": 2, "69": 3, "78": 3, "79": 5, "80": 5, "81": 33, "82": 34, "83": 35, "84": 35, "85": 35, "86": 35, "87": 36, "88": 36, "89": 36, "90": 36, "91": 37, "92": 37, "93": 38, "94": 38, "95": 41, "101": 95}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557103691.4628546
_enable_loop = True
_template_filename = 'C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/film.html'
_template_uri = 'film.html'
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
        img = context.get('img', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        episode_id = context.get('episode_id', UNDEFINED)
        sequence_id = context.get('sequence_id', UNDEFINED)
        def tag():
            return render_tag(context._locals(__M_locals))
        release_date = context.get('release_date', UNDEFINED)
        title = context.get('title', UNDEFINED)
        opening_crawl = context.get('opening_crawl', UNDEFINED)
        director = context.get('director', UNDEFINED)
        self = context.get('self', UNDEFINED)
        producer = context.get('producer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tag'):
            context['self'].tag(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tag(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def tag():
            return render_tag(context)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        img = context.get('img', UNDEFINED)
        def content():
            return render_content(context)
        episode_id = context.get('episode_id', UNDEFINED)
        sequence_id = context.get('sequence_id', UNDEFINED)
        release_date = context.get('release_date', UNDEFINED)
        title = context.get('title', UNDEFINED)
        opening_crawl = context.get('opening_crawl', UNDEFINED)
        director = context.get('director', UNDEFINED)
        self = context.get('self', UNDEFINED)
        producer = context.get('producer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<section class="single_product_details_area d-flex align-items-center">\r\n\r\n    <!-- Single Product Thumb -->\r\n    <div class="single_product_thumb clearfix">\r\n        <div style="margin-top: 0.5px">\r\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(img))
        __M_writer('">  \r\n        </div>  \r\n    </div>\r\n\r\n    <!-- Single Product Description -->\r\n    <div class="single_product_desc clearfix">\r\n        <h2>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(title))
        __M_writer('</h2>\r\n        <p class="product-price">Episode Number: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(episode_id))
        __M_writer('</p>\r\n        <p class="product-desc">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opening_crawl))
        __M_writer('</p>\r\n        <h5>Director: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(director))
        __M_writer('</h5>\r\n        <h5>Producer: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(producer))
        __M_writer('</h5>\r\n        <h5>Release Date: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(release_date))
        __M_writer('</h5>\r\n        <br>\r\n        <a class="btn essence-btn" href="/homepage/index">Back to the List</a>\r\n        <nav aria-label="navigation">\r\n            <ul class="pagination mt-50 mb-70">\r\n')
        if sequence_id > 1:
            __M_writer('                    <li class="page-item"><a class="page-link" href="/homepage/film/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sequence_id - 1))
            __M_writer('"><i class="fa fa-angle-left"></i></a></li>\r\n')
        if sequence_id < 7:
            __M_writer('                    <li class="page-item"><a class="page-link" href="/homepage/film/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sequence_id + 1))
            __M_writer('"><i class="fa fa-angle-right"></i></a></li>\r\n')
        __M_writer('            </ul>\r\n        </nav>\r\n    </div>\r\n</section>\r\n<!-- ##### Single Product Details Area End ##### -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/film.html", "uri": "film.html", "source_encoding": "utf-8", "line_map": {"29": 0, "47": 1, "52": 2, "57": 36, "63": 2, "71": 2, "77": 3, "92": 3, "93": 9, "94": 9, "95": 15, "96": 15, "97": 16, "98": 16, "99": 17, "100": 17, "101": 18, "102": 18, "103": 19, "104": 19, "105": 20, "106": 20, "107": 25, "108": 26, "109": 26, "110": 26, "111": 28, "112": 29, "113": 29, "114": 29, "115": 31, "121": 115}}
__M_END_METADATA
"""

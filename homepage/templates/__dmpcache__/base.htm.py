# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557103722.461852
_enable_loop = True
_template_filename = 'C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['tag', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def tag():
            return render_tag(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n\r\n<head>\r\n\r\n    <title>\r\n        SWAPI - ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tag'):
            context['self'].tag(**pageargs)
        

        __M_writer('\r\n    </title>\r\n\r\n')
        __M_writer('    <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n    <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">\r\n    <script src="https://kryogenix.org/code/browser/sorttable/sorttable.js"></script>\r\n\r\n    <!-- jQuery library -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/jquery/jquery-2.2.4.min.js"></script>\r\n\r\n    <!-- Popper JS -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/popper.min.js"></script>\r\n\r\n    <!-- Core Style CSS -->\r\n    <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/css/core-style.css">\r\n    <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/star-wars-icon-vector-2.jpg">\r\n\r\n</head>\r\n    <body>\r\n        <!-- ##### Header Area Start ##### -->\r\n        <header class="header_area">\r\n            <div class="classy-nav-container breakpoint-off d-flex align-items-center justify-content-between">\r\n                <!-- Classy Menu -->\r\n                <nav class="classy-navbar" id="essenceNav">\r\n                    <!-- Logo -->\r\n                    <a class="nav-brand" href="/"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/star-wars-icon-vector-13.jpg" alt="" style="max-height: 50px;"></a>\r\n                    <!-- Navbar Toggler -->\r\n                    <div class="classy-navbar-toggler">\r\n                        <span class="navbarToggler"><span></span><span></span><span></span></span>\r\n                    </div>\r\n                    <!-- Menu -->\r\n                    <div class="classy-menu">\r\n                        <!-- close btn -->\r\n                        <div class="classycloseIcon">\r\n                            <div class="cross-wrap"><span class="top"></span><span class="bottom"></span></div>\r\n                        </div>\r\n                        <!-- Nav Start -->\r\n                        <div class="classynav">\r\n                            <ul>\r\n                                <li><a href="/homepage/index/">Film List</a></li>\r\n                                <li><a href="#">Films</a>\r\n                                    <ul class="dropdown">\r\n')
        for film in request.session['films']:
            __M_writer('                                        <li><a href="/homepage/film/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[3]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(film[0]))
            __M_writer('</a></li>\r\n')
        __M_writer('                                    </ul>\r\n                                </li>\r\n                            </ul>\r\n                        </div>\r\n                        <!-- Nav End -->\r\n                    </div>\r\n                </nav>\r\n            </div>\r\n        </header>\r\n        <!-- ##### Header Area End ##### -->\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer class="footer_area clearfix">\r\n            <div class="container">\r\n                <div class="row">\r\n                    <div class="col-md-4"></div>\r\n                    <div class="col-md-4 text-center">\r\n                        <a href="/"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/SWLogo.svg" alt="" style="max-height: 300px;"></a>\r\n                    </div>\r\n                    <div class="col-md-4"></div>\r\n                </div>\r\n                <div class="row mt-5">\r\n                    <div class="col-md-12 text-center">\r\n                        <p>\r\n                            <!-- Link back to Colorlib can\'t be removed. Template is licensed under CC BY 3.0. -->\r\n                            Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>\r\n                            <!-- Link back to Colorlib can\'t be removed. Template is licensed under CC BY 3.0. -->\r\n                        </p>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </footer>\r\n    </body>\r\n    <!-- Bootstrap js -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/bootstrap.min.js"></script>\r\n    <!-- Plugins js -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/plugins.js"></script>\r\n    <!-- Classy Nav js -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/classy-nav.min.js"></script>\r\n    <!-- Active js -->\r\n    <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/active.js"></script>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tag(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tag():
            return render_tag(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/eddy0/Desktop/Swapi/swapi/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "30": 2, "35": 9, "36": 13, "37": 14, "38": 14, "39": 20, "40": 20, "41": 23, "42": 23, "43": 26, "44": 26, "45": 27, "46": 27, "47": 37, "48": 37, "49": 54, "50": 55, "51": 55, "52": 55, "53": 55, "54": 55, "55": 57, "60": 68, "61": 76, "62": 76, "63": 93, "64": 93, "65": 95, "66": 95, "67": 97, "68": 97, "69": 99, "70": 99, "76": 9, "87": 68, "98": 87}}
__M_END_METADATA
"""

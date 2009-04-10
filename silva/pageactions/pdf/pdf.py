# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope import component

from silva.pageactions.base.base import PageAction
from silva.core.views import views as silvaviews

from five import grok

import popen2


class PDFPage(silvaviews.Template):

    grok.name('index.pdf')

    def pdf(self):
        """Convert the current page as a PDF.
        """

        print_html = component.getMultiAdapter((self.context, self.request),
                                               name='print.html')()
        print_html = print_html.encode('cp1252', 'replace')
        (stdout, stdin) = popen2.popen2((
            """htmldoc --charset cp-1252 --header . --fontsize 10 --bodyfont helvetica """
            """--webpage -t pdf --quiet --jpeg - """))

        stdin.write(print_html)
        stdin.close()

        pdf = stdout.read()
        stdout.close()
        return pdf

    def render(self):
        """Converts a HTML-Page to a PDF-Document.
        """

        pdf = self.pdf()
        self.response.setHeader('Content-type', 'application/pdf')
        self.response.setHeader(
            'Content-disposition', 'inline; filename="%s.pdf"' % (self.context.getId()))
        return pdf


class PDFAction(PageAction):

    grok.order(30)

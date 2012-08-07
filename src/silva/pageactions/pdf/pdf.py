# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

import subprocess

from five import grok
from silva.core.views import views as silvaviews
from silva.core.views.httpheaders import ResponseHeaders
from zope.publisher.interfaces.browser import IBrowserRequest
from silva.pageactions.base.base import PageAction
from zope.component import getMultiAdapter


class PDFPage(silvaviews.View):
    grok.name('index.pdf')

    def pdf(self):
        """Convert the current page as a PDF.
        """
        html_view = getMultiAdapter(
            (self.context, self.request), name='print.html')
        html_print = html_view().encode('cp1252', 'replace')
        command = subprocess.Popen(
            """htmldoc --charset cp-1252 --header . --fontsize 10 """
            """--bodyfont helvetica --webpage -t pdf --quiet --jpeg - """,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        pdf, error = command.communicate(input=html_print)
        return pdf

    def render(self):
        """Converts a HTML-Page to a PDF-Document.
        """
        return self.pdf()


class PDFResponseHeader(ResponseHeaders):
    grok.adapts(IBrowserRequest, PDFPage)

    def other_headers(self, headers):
        identifier = self.context.context.getId()
        self.response.setHeader(
            'Content-type',
            'application/pdf')
        self.response.setHeader(
            'Content-disposition',
            'inline; filename="%s.pdf"' % identifier)


class PDFAction(PageAction):
    grok.order(30)

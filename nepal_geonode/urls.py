# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView

from geonode.urls import urlpatterns

# Text to put at the end of each page's <title>.
admin.site.site_title = 'Nepal GeoNode Site Admin'
# Text to put in each page's <h1>.
admin.site.site_header = 'Nepal GeoNode Administration'
# Text to put at the top of the admin index page.
admin.site.index_title = 'Nepal GeoNode'


urlpatterns += (
    # include your urls here

)

urlpatterns = patterns('',
                       url(r'^/?$',
                           TemplateView.as_view(template_name='site_index.html'),
                           name='home'),
                       ) + urlpatterns

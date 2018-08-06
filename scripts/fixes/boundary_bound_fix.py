
from geonode.layers.models import *
from geonode.base.models import Link
import re

from django.db import connection
cursor = connection.cursor()
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

def format_link(ly, link_str):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link_str)
    x0 = str(ly.bbox_x0)
    y0 = str(ly.bbox_y0)
    x1 = str(ly.bbox_x1)
    y1 = str(ly.bbox_y1)
    flag_set = False
    for url in urls:
        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        bbox = query.get("bbox")
        if bbox:
            new_bbox = x0+","+y0+","+x1+"," + y1
            query["bbox"] = new_bbox
            url_parts[4] = urlencode(query)
            new_url = urlparse.urlunparse(url_parts)
            link_str = link_str.replace(url, new_url)
            flag_set = True
    if flag_set:
        return True, link_str
    return False, link_str

layers = Layer.base_objects.all()


for l in layers:
    csw_anytext = l.csw_anytext
    metadata_xml = l.metadata_xml
    flag_set = False
    if csw_anytext:
        changed, csw_anytext = format_link(l, csw_anytext)
        if changed:
            flag_set = True

    if metadata_xml:
        changed, metadata_xml = format_link(l, metadata_xml)
        if changed:
            flag_set = True

    if flag_set:
        sql_query = "UPDATE base_resourcebase SET csw_anytext=%s, metadata_xml=%s WHERE id=%s;"
        cursor.execute(sql_query,(csw_anytext, metadata_xml, l.id))

    links = Link.objects.filter(resource__id=l.id)
    for link in links:
        link_url = link.url
        if link_url:
            changed, link_url = format_link(l, link_url)
        if changed:
            link.url = link_url
            link.save()




from geonode.layers.models import Layer
from geonode.base.models import License, TopicCategory
import csv

rows = csv.DictReader(open("./scripts/fixes/import_meta_data_osm_layers/nepal_osm.csv"))
license = License.objects.get(id=6)
for row in rows:
    layer_name = row.get("name")
    layer = Layer.objects.filter(name=layer_name, store="nepal_osm")
    if not layer.exists():
        print(layer_name, " not found")
        continue
    layer = layer[0]
    layer.title = row.get("title")
    layer.license = license
    layer.abstract = row.get("abstract")
    category = TopicCategory.objects.get(identifier=row.get("catname"))
    layer.category = category
    layer.save()


default_abstract = """Airports (polygon) (OSM latest extract)","This data is extracted from the OpenStreetMap database on a daily basis at 12:01 AM Nepal Standard Time (UTC +5:45). The data is automatically filtered into pre-selected feature categories. 
 
OpenStreetMap is a worldwide open geospatial database, roughly equivalent to Wikipedia but for maps. It can be edited, checked and downloaded by anyone agreeing to abide by the terms of the Open Data Commons Open Database License (ODBl). Please note that the dataset is only as complete as the underlying OpenStreetMap database and quality across Nepal may be highly variable.
 
If you feel that the feature categories miss an important subset of data or misrepresent the reality of Nepal, please write to a GeoNode admin explaining the features you’d like to see. If the proposed category appears useful and possible to create we will modify the export automation accordingly. Alternately, you can create your own custom export at export.hotosm.org.
 
All data © OpenStreetMap contributors.
","transportation"
"banks","Banks (OSM latest extract)","This data is extracted from the OpenStreetMap database on a daily basis at 12:01 AM Nepal Standard Time (UTC +5:45). The data is automatically filtered into pre-selected feature categories. 
 
OpenStreetMap is a worldwide open geospatial database, roughly equivalent to Wikipedia but for maps. It can be edited, checked and downloaded by anyone agreeing to abide by the terms of the Open Data Commons Open Database License (ODBl). Please note that the dataset is only as complete as the underlying OpenStreetMap database and quality across Nepal may be highly variable.
 
If you feel that the feature categories miss an important subset of data or misrepresent the reality of Nepal, please write to a GeoNode admin explaining the features you’d like to see. If the proposed category appears useful and possible to create we will modify the export automation accordingly. Alternately, you can create your own custom export at export.hotosm.org.
 
All data © OpenStreetMap contributors.
"""

osm_layers = Layer.objects.filter(store="nepal_osm", title__icontains="_")
for osm_layer in osm_layers:
    layer.title = osm_layers[0].title.replace("_", " ").title()
    layer.license = license
    layer.abstract = row.get("abstract")
    category = TopicCategory.objects.get(identifier="location")
    layer.category = category
    layer.save()




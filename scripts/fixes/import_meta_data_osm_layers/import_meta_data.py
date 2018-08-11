from geonode.layers.models import Layer, License, TopicCategory
from geonode.layers.forms import LayerForm, LayerUploadForm, NewLayerUploadForm, LayerAttributeForm
from geonode.base.forms import CategoryForm, TKeywordForm
import csv
rows = csv.DictReader(open("./nepal_osm.csv"))
license = License.objects.ge(id=6)
for row in rows:
	layer_name = row.get("name")
	layer = Layer.objects.get(name=layer_name)
	layer.title = row.get("title")
	layer.license = license
	layer.abstract = row.get("abstract")
	category = TopicCategory.objects.get(identifier=row.get("catname"))
	layer.category = category
	layer.save()


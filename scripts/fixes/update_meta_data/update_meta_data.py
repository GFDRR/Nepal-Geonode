from geonode.layers.models import Layer
from geonode.base.models import License, TopicCategory
import csv

rows = csv.DictReader(open("./scripts/fixes/update_meta_data/new_meta_data.csv"))
# license = License.objects.get(id=6)

for row in rows:
    layer_id = row.get("id")
    layer = Layer.objects.filter(id=layer_id, store="nepal_osm")
    if not layer.exists():
        print(layer_id, " not found")
        continue
    print("found")
    continue
    layer = layer[0]

    layer.abstract = row.get("new_metadata")

    layer.save()





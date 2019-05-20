from geonode.layers.models import Layer
from geonode.base.models import License, TopicCategory
import csv
import pandas as pd
file_path = "./scripts/fixes/update_meta_data/new_meta_data.csv"
df= pd.read_csv(file_path)
for index, row in df.iterrows():
    layer_id = row.id
    layer = Layer.objects.filter(alternate=layer_id)
    if not layer.exists():
        print(layer_id, " not found")
        continue
    print("found")
    print(row.new_metadata)
    continue
    layer = layer[0]

    layer.abstract = row.get("new_metadata")

    layer.save()





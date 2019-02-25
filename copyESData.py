import json
from elasticsearch import Elasticsearch

es = Elasticsearch(["localhost:9200"], http_compress=True)

casts = es.search(index='casts')
print(casts)

from elasticsearch import Elasticsearch
import json

url = '#'
user = '#'
password = '#'
es_client = Elasticsearch(url, http_auth=(user, password))
index = 'amz_test'
# body = """
# {
#   "query": {
#     "match": {
#       "name": "ZHANG"
#     }
#   }
# }
# """
#  # 查询
# response = es_client.search(index=index, body=body)
# print(response)

# 更新
# body = """
# {
#   "doc": {
#     "name": "QIAN"
#   }
# }
# """
# response = es_client.update(index=index, body=body, id=3)
# print(response)

# 插入
# body = """
# {
#   "doc": {
#     "name": "LI"
#   },
#   "doc_as_upsert": true
# }
# """
# response = es_client.update(index=index, body=body, id=6)
# print(response)

# 批量更新
body_list = [
    '{ "update" : {"_id" : "1", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value1"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "2", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value2"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "3", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value3"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "4", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value4"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "5", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value5"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "6", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value6"}, "doc_as_upsert": true }',
    '{ "update" : {"_id" : "7", "_index" : "amz_bulk"} }\r\n{ "doc" : {"field2" : "value7"}, "doc_as_upsert": true }',
]
body = '\r\n'.join([result for result in body_list])
response = es_client.bulk(body=body)
print(json.dumps(response))

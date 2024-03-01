import os

from elasticsearch import Elasticsearch
from datetime import datetime
from icecream import ic

def get_netflow_resampled(start_time: str, end_time: int, elastic_host: str, elastic_index: str) -> list:
    while True:
        response = Elasticsearch(hosts=["https://"+elastic_host+":9200"], ca_certs="/etc/elasticsearch/certs/http_ca.crt", basic_auth=("elastic","f*xBBTke-ytKJkVoZ0+M")).search(
            index=elastic_index,
            body={
                "size": 0,
                "query": {
                    "range": {
                        "@timestamp": {
                            "gte": "now-{}s".format(end_time),
                            "lte": start_time
                        }
                    }
                },
                "aggs": {
                    "all_attributes": {
                        "date_histogram": {
                            "field": "@timestamp",
                            "fixed_interval": "{}s".format(end_time)
                        },
                        "aggs": {
                            "packets": {
                                "sum": {
                                    "field": "netflow.packet_delta_count"
                                }
                            },
                            "USIP": {
                                "cardinality": {
                                    "field": "netflow.source_ipv4_address"
                                }
                            },
                            "UDIP": {
                                "cardinality": {
                                    "field": "netflow.destination_ipv4_address"
                                }
                            },
                            "UPR": {
                                "cardinality": {
                                    "field": "netflow.protocol_identifier"
                                }
                            }
                        }
                    }
                }
            }
        )
        # print(str(response["aggregations"]z["all_attributes"]["buckets"])+"\n\n")
        if len(response["aggregations"]["all_attributes"]["buckets"])>0:
            return response["aggregations"]["all_attributes"]["buckets"]
        else:
            continue


def get_netflow_data_at_nearest_time(time: int, elastic_host: str, elastic_index: str, is_after=True) -> dict:
    # print(time)
    # print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%dT%H:%M:%S.000Z'))
    response = Elasticsearch(hosts=["https://"+elastic_host+":9200"], ca_certs="/etc/elasticsearch/certs/http_ca.crt", basic_auth=("elastic","f*xBBTke-ytKJkVoZ0+M")).search(
        index=elastic_index,
        body={
            "size": 1,
            "query": {
                "match": {
                    "@timestamp": datetime.utcfromtimestamp(time).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                }
            },
            "_source": [
                "netflow.source_ipv4_address",
                "netflow.destination_ipv4_address",
                "netflow.destination_transport_port",
                "netflow.protocol_identifier"
            ]
        }
    )
    # print(str(response)+"\n\n")
    if response['hits']['total']['value'] > 0 and 'netflow' in response['hits']['hits'][0]['_source']:
        return response['hits']['hits'][0]['_source']['netflow']
    else:
        return get_netflow_data_at_nearest_time(time + 1 if is_after is True else time - 1, elastic_host, elastic_index)

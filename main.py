from retia_api.operation import *
from retia_api.views import detector_start

global_ipaddr="172.16.0.1"
global_port="443"
global_auth=("retia", "retia00!")
global_header={"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}
conn_strings={"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}

# print(getInterfaceList({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}))
# print(getInterfaceDetail({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth},req_to_show={"name":"GigabitEthernet1"}))
# print(static_routing.set(global_ipaddr, global_port, global_auth, global_header, [{"destin        rule_to_change=[]
# ation-prefix":"0.0.0.0/0", "next-hop-address":"192.168.137.2"}]))
# print(getHostname({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}))
# print(check_device_connection({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}))
# print(createOspfProcess({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}, {"id":10}))
# print(setOspfProcessDetail({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}, {"id":10, "default-information-originate":"true", "network":[{"ip":"10.0.0.4","wildcard":"0.0.0.3","area":0},{"ip":"10.0.0.8","wildcard":"0.0.0.3","area":0}],"passive-interface":["GigabitEthernet1","GigabitEthernet4","GigabitEthernet5"],"redistribute":["connected"]}))
# print(delOspfProcess({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}, {"id":10}))
# print(getOspfProcessDetail({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth},{"id":10}))

# print(setInterfaceDetail({"ipaddr": global_ipaddr, "port": global_port, "credential": global_auth}, {"name":"GigabitEthernet2", "enabled":True, "ip":"10.0.0.5", "netmask":"255.255.255.252"}))

# print(getAclList(conn_strings=conn_strings, req_to_show={"name":"INI2"}))
# print(setAclDetail(conn_strings=conn_strings, req_to_change={'name': 'INI2', 'rules': [{'sequence': '10', 'action': 'permit', 'prefix': '9.9.9.9', 'wildcard': "0.0.0.3"},{"sequence":20, 'action':"deny","prefix":"any","wildcard":None}]}))

# print(json.loads(getSomething(conn_strings, "/interface/GigabitEthernet=5/ip/flow/monitor").text))
# print(add_netflow_config(conn_strings=conn_strings, req_to_create={}))
# print(json.loads(getSomething(conn_strings=conn_strings, path="/flow/exporter=RETIA_EXPORTER").text))

# print(check_device_detector_config(conn_strings=conn_strings, req_to_check={"device_interface_to_filebeat":"GigabitEthernet4", "filebeat_host": "172.16.0.2", "filebeat_port": 50255}))
# print(del_device_detector_config(conn_strings, {"device_interface_to_server":"GigabitEthernet5"}))

getMonitorDetail()

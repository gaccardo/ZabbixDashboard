# coding: utf8
# intente algo como

import pyzabbix

def index():
	return dict()

def hosts():
  zapi = pyzabbix.ZabbixAPI(auth.zabbix_host)
  zapi.login(auth.zabbix_user, auth.zabbix_pass)

  hosts = zapi.host.get(output="extend")
  final_hosts = list()

  for host in hosts:
    items = zapi.item.get(filter = {'hostid': host['hostid']}, 
                          output="extend")
    final_hosts.append({'host': host, 'items': items})
 
  return dict(hosts=final_hosts)

def dashboards():
  query = db( db.dashboard.id > 0 ).select()
  return dict(dashboards=query)

def dashboard():
  zapi = pyzabbix.ZabbixAPI(auth.zabbix_host)
  zapi.login(auth.zabbix_user, auth.zabbix_pass)
  query = list()
  items = list()

  if request.vars.dashid:
    query = db( (db.dashboard.id == db.graphbox.dashboard) & \
                (db.dashboard.id == request.vars.dashid) ).select()

    for graph in query:
      item = zapi.item.get(filter = {'itemid': graph.graphbox.itemid},
                           output="extend")

      host = zapi.host.get(filter = {'hostid': item[0]['hostid']},
                       output="extend")

      temp = {'value': item[0]['lastvalue'],
              'prevvalue': item[0]['prevvalue'],
              'name': item[0]['name'],
              'key': item[0]['key_'],
              'unit': item[0]['units'],
              'itemid': item[0]['itemid'],
              'hostname': host[0]['name']}

      items.append(temp)
    
    dashboard = dict()
    dashboard['maxNum'] = query[0].dashboard.maxNum
    dashboard['greenFrom'] = query[0].dashboard.greenFrom
    dashboard['greenTo'] = query[0].dashboard.greenTo
    dashboard['yellowFrom'] = query[0].dashboard.yellowFrom
    dashboard['yellowTo'] = query[0].dashboard.yellowTo
    dashboard['redFrom'] = query[0].dashboard.redFrom
    dashboard['redTo'] = query[0].dashboard.redTo
    dashboard['name'] = query[0].dashboard.name
    
  return dict(graphs=items, dashboard=dashboard)

def graphs_by_dashboard():
  zapi = pyzabbix.ZabbixAPI(auth.zabbix_host)
  zapi.login(auth.zabbix_user, auth.zabbix_pass)
  query = list()
  items = list()
  chart = dict()
  chart['chart'] = dict()
  chart['dials'] = dict()
  chart['dials']['dial'] = list()

  if request.vars.dashid:
    query = db( (db.dashboard.id == db.graphbox.dashboard) & \
                (db.dashboard.id == request.vars.dashid) ).select()

    for graph in query:
      item = zapi.item.get(filter = {'itemid': graph.graphbox.itemid},
                           output="extend")

      host = zapi.host.get(filter = {'hostid': item[0]['hostid']},
                       output="extend")

      temp = {'value': item[0]['lastvalue'],
              'borderalpha': "0",
              'bgcolor': "000000",
              'basewidth': "28",
              'topwidth': "1",
              'radius': "130"}

      chart['dials']['dial'].append(temp)

      items.append(temp)

    chart['colorrange'] = dict()
    chart['colorrange']['color'] = list()
    chart['colorrange']['color'].append({
      "minvalue": "0",
      "maxvalue": "1600",
      "code": "399E38"
      })
    chart['colorrange']['color'].append({
      "minvalue": "1600",
      "maxvalue": "2000",
      "code": "E48739"
      })
    chart['colorrange']['color'].append({
      "minvalue": "2000",
      "maxvalue": "2100",
      "code": "B41527"
      })
    chart['chart']['manageresize'] = "1"
    chart['chart']['origw'] = "400"
    chart['chart']['origh'] = "250"
    chart['chart']['managevalueoverlapping'] = "1"
    chart['chart']['autoaligntickvalues'] = "1"
    chart['chart']['bgcolor'] = "AEC0CA,FFFFFF"
    chart['chart']['fillangle'] = "45"
    chart['chart']['upperlimit'] = "2500000"
    chart['chart']['lowerlimit'] = "1600000"
    chart['chart']['majortmnumber'] = "10"
    chart['chart']['majortmheight'] = "8"
    chart['chart']['showgaugeborder'] = "0"
    chart['chart']['gaugeouterradius'] = "140"
    chart['chart']['gaugeoriginx'] = "205"
    chart['chart']['gaugeoriginy'] = "206"
    chart['chart']['gaugeinnerradius'] = "2"
    chart['chart']['formatnumberscale'] = "1"
    chart['chart']['numberprefix'] = "$"
    chart['chart']['decmials'] = "2"
    chart['chart']['tickmarkdecimals'] = "1"
    chart['chart']['pivotradius'] = "17"
    chart['chart']['showpivotborder'] = "1"
    chart['chart']['pivotbordercolor'] = "000000"
    chart['chart']['pivotborderthickness'] = "5"
    chart['chart']['pivotfillmix'] = "FFFFFF,000000"
    chart['chart']['tickvaluedistance'] = "10"
    chart['annotations'] = dict()
    chart['annotations']['groups'] = list()
    chart['annotations']['groups'].append(dict())
    chart['annotations']['groups'][0]['x'] = "205"
    chart['annotations']['groups'][0]['y'] = "207.5"
    chart['annotations']['groups'][0]['items'] = list()
    chart['annotations']['groups'][0]['items'].append({
      "type": "circle",
      "x": "0",
      "y": "2.5",
      "radius": "150",
      "startangle": "0",
      "endangle": "180",
      "fillpattern": "linear",
      "fillasgradient": "1",
      "fillcolor": "dddddd,666666",
      "fillalpha": "100,100",
      "fillratio": "50,50",
      "fillangle": "0",
      "showborder": "1",
      "bordercolor": "444444",
      "borderthickness": "2"     
      })
    chart['annotations']['groups'][0]['items'].append({
      "type": "circle",
      "x": "0",
      "y": "0",
      "radius": "145",
      "startangle": "0",
      "endangle": "180",
      "fillpattern": "linear",
      "fillasgradient": "1",
      "fillcolor": "666666,ffffff",
      "fillalpha": "100,100",
      "fillratio": "50,50",
      "fillangle": "0",     
      })
    
  return chart

def fusiondashboard():
  return dict()
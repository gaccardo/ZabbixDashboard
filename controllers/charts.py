# coding: utf8

import pyzabbix

def angular_gauge():
	dashboard_query = db( db.dashboard.id == request.vars.dashid).select()
	item_query = db( (db.graphbox.itemid == request.vars.id) ).select()

	chart_json = dict()

	chart_json["chart"] = dict()
	chart_json["chart"]["lowerlimit"] = "0"
	chart_json["chart"]["upperlimit"] = "%s" % item_query[0]['maxNum']
	#chart_json["chart"]["lowerlimitdisplay"] = "Bad"
	#chart_json["chart"]["upperlimitdisplay"] = "Good"
	chart_json["chart"]["numbersuffix"] = "%s" % item_query[0]['itemprefix']
	chart_json["chart"]["showvalue"] = "1"
	chart_json["chart"]["dataStreamURL"] = URL('charts', 'angular_gauge_input_data',
	                                           vars={'id': request.vars.id})
	chart_json["chart"]["refreshInterval"] = "10"
	chart_json["chart"]["tickValueDistance"] = "25"
	chart_json["chart"]["showGaugeBorder"] = "1"
	chart_json["chart"]["pivotRadius"] = "10"
	chart_json["chart"]["valueBelowPivot"] = "1"
	chart_json["chart"]["baseFontSize"] = "25"
	

	chart_json["colorrange"] = dict()
	chart_json["colorrange"]["color"] = [{"minvalue": "%s" % item_query[0]['greenFrom'],
	                                      "maxvalue": "%s" % item_query[0]['greenTo'],
	                                      "code": "8BBA00"},
	                                     {"minvalue": "%s" % item_query[0]['yellowFrom'],
	                                      "maxvalue": "%s" % item_query[0]['yellowTo'],
	                                      "code": "F6BD0F"},
	                                     {"minvalue": "%s" % item_query[0]['redFrom'],
	                                      "maxvalue": "%s" % item_query[0]['redTo'],
	                                      "code": "FF654F"}]


	chart_json["dials"] = dict()
	chart_json["dials"]["dial"] = [{"value": "0",
	                                "baseWidth": "20",
	                                "topWidth": "4",
	                                "valueX": "270",
	                                "valueY": "140",}]

	return chart_json

def angular_gauge_input_data():
	zapi = pyzabbix.ZabbixAPI(auth.zabbix_host)
	zapi.login(auth.zabbix_user, auth.zabbix_pass)

	item = zapi.item.get(filter = {'itemid': request.vars.id},
                       output="extend")

	return "&value=%s" % item[0]['lastvalue']
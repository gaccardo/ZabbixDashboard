# coding: utf8
# intente algo como

import pyzabbix

def dashboards():
  query = db( db.dashboard.id > 0 ).select()
  return dict(dashboards=query)

def dashboard():
  dashboard_query = db( db.dashboard.id == request.vars.dashid).select()
  items_query = db( db.dashboard.id == db.graphbox.dashboard ).select()

  return dict(name=dashboard_query[0]["name"], items=items_query)
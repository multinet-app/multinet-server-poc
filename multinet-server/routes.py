import views

import logging
logger = logging.getLogger(__name__)

def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_get('/db/{name}', views.getDB)
    app.router.add_post('/db/{name}', views.addDB)
    app.router.add_get('/graph/{db_name}/{name}', views.getGraph)
    app.router.add_post('/graph/{db_name}/{name}', views.addGraph)
    app.router.add_get('/vertices/{db_name}/{graph_name}/{name}', views.getVertices)
    app.router.add_post('/vertices/{db_name}/{graph_name}/{name}', views.addVertices)
    app.router.add_get('/edges/{db_name}/{graph_name}/{name}', views.getEdges)
    app.router.add_post('/edges/{db_name}/{graph_name}/{name}', views.addEdges)

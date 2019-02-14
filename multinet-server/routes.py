import views

import logging
logger = logging.getLogger(__name__)

def setup_routes(app):
    app.router.add_get('/', views.index)

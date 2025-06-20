# -*- coding: utf-8 -*-
{
    "name": "Taller Mecánico",
    "summary": "Gestión completa de taller mecánico con diagnósticos, clientes y automóviles",
    "description": """
        Este módulo permite gestionar un taller mecánico completo con:
        - Registro de diagnósticos de automóviles
        - Gestión de clientes
        - Catálogo de automóviles con marcas, modelos y tipos
        - Reportes PDF de diagnósticos
        - Configuración de marcas, modelos y tipos de vehículos
    """,
    "author": "Edgar de la Cruz",
    "support": "edgargdcv@gmail.com",
    "website": "https://allity.com/",
    "company": "Allity",
    "maintainer": "Edgar de la Cruz",
    'category': 'Industries',
    "version": "18.0.1.0",
    "depends": [
        "base",
        "hr",
        "mail"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/vehicle_brand_views.xml",
        "views/vehicle_model_views.xml",
        "views/vehicle_type_views.xml",
        "views/vehicle_views.xml",
        "views/diagnostic_views.xml",

        "views/menu_views.xml",
        "report/diagnostic_templates.xml",
        "report/diagnostic_report.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "license": "OPL-1",
    "installable": True,
    "application": True,
}

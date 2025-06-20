{
    'name': 'Rick and Morty API Sync',
    'summary': 'Synchronization of characters from Rick and Morty API',
    'description': """
This module allows you to synchronize characters from the Rick and Morty
series from the public API https://rickandmortyapi.com/

Features:
- Model to store characters (name and image)
- Manual synchronization from list view
- Automatic image download
    """,
    'author': 'Edgar de la Cruz',
    'support': 'edgargdcv@gmail.com',
    'website': 'https://allity.com',
    'company': 'Allity',
    'maintainer': 'Edgar de la Cruz',
    'category': 'Tools',
    'version': '18.0.1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/rick_morty_character_views.xml',
        'wizards/sync_wizard_views.xml',
        'views/menu_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
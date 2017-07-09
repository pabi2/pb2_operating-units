# -*- coding: utf-8 -*-
{
    "name": "PABI Asset Management Operating Unit",
    "version": "1.0",
    "license": 'AGPL-3',
    "author": "Kitti U.",
    "category": "Asset Management",
    "depends": ["pabi_asset_management",
                "operating_unit",
                ],
    "description": """
Adds a the operating unit to

- Asset Request
    """,
    "data": [
        "views/asset_request_view.xml",
        "security/asset_request_security.xml"
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
}

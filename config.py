from secret import MONGODB_CONNECTION_URL


DATABASES = {
    'CSV': {
        'MAPPER': 'standards'
    },
    'MONGODB': {
        'name': 'adsDB',
        'connection_url': MONGODB_CONNECTION_URL,
        'collections': [
            'morizon',
            'otodom'
        ]
    },
}

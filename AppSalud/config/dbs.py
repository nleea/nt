from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DBS = {
    "SQL-lite":{
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    },
    "MONGO":{
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'db0',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': "mongodb+srv://nelson:xyz3602@db0.mcgx82i.mongodb.net/db_1?retryWrites=true&w=majority"
            }  
        }}
}
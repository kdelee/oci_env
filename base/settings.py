# Pulp needs an /etc/pulp/settings.py with CONTENT_ORIGIN to start.
import sys
sys.path.insert(0, '/src')
CONTENT_ORIGIN='http://localhost:5001'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pulp',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pulp',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'pulp_pg_replica',
        'PORT': 5432,
    },
}
DATABASE_ROUTERS = ['pulpcore.app.local_read_router.MavenReadReplicaRouter']
SECRET_KEY='local-pulp-experiment-secret-key'
CACHE_ENABLED=True
MAVEN_PACKAGE_COUNT_CACHE_ENABLED=True
MAVEN_PACKAGE_PAGE_CACHE_ENABLED=True
REDIS_HOST='localhost'
REDIS_PORT=6379

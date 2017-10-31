DATABASES = {
    'default': {
      'ENGINE': 'sql_server.pyodbc',
      'NAME': 'TEST_MICHIYA',
      'USER': 'username',
      'PASSWORD': 'password',
      'HOST': 'example.us-west-2.rds.amazonaws.com',
      'PORT':'1433',
      'OPTIONS': {
        'host_is_server': True,
        # https://github.com/michiya/django-pyodbc-azure/issues/64
        'unicode_results': True,
        'extra_params': 'tds_version=8.0',
        'use_legacy_datetime': True,
      },
    }

}

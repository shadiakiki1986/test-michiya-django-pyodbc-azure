# test-michiya-django-pyodbc-azure
Example django project showing issue with [michiya/django-pyodbc-azure#116](https://github.com/michiya/django-pyodbc-azure/issues/116)

## Installation

    git clone https://github.com/shadiakiki1986/test-michiya-django-pyodbc-azure
    sudo pip3 install pew
    pew new -i django -i django-pyodbc-azure TEST_MDPA

## Usage

1. Do initial test on sqlite3 (will work)

```bash
    ./manage.py migrate # initial migration
    ./manage.py createsuperuser
    ./manage.py loaddata --app app demo.json # load sample data
```

2. Launch

```bash
    ./manage.py runserver # serve project
```

3. Browse to admin "level 2" change page at http://localhost/admin/app/level3/1/change/

  - This will work fine

4. Run the test: `./manage.py test proj.app.tests`

  - This test shall pass

5. Modify the host, username, password in `proj/settings_production.py`.

  - This will change the django project from using sqlite3 to using SQL server backend with `django-pyodbc-azure`.

6. Uncomment the line `from .settings_production import *` from `proj/settings.py`

7. Repeat the migrate, createsuperuser, loaddata, runserver above.

8. Browse to the same page.

  - This will result in exception `('24000', '[24000] [FreeTDS][SQL Server]Invalid cursor state (0) (SQLFetch)')`

9. Run the test: `./manage.py test proj.app.tests`

  - This test shall not pass


## Dev notes

     1607  pip install django django-pyodbc-azure
     1627  django-admin startproject proj .
     1628  mkdir proj/app
     1629  django-admin startapp app proj/app
     1632  vim proj/settings.py # add proj.app to installed apps + * to allowed hosts

     ./manage.py dumpdata app > data.json

## scrapy-state

See CHANGELOG.md for detail description.



### Getting Help


### QuickStart
```bash
python3 -m pip install -U scrapy-state
```


### Installing from Github

```bash
python3 -m pip install -U https://github.com/alex-ber/scrapy-state/archive/master.zip
```
Optionally installing tests requirements.

```bash
python3 -m pip install -U https://github.com/alex-ber/scrapy-state/archive/master.zip#egg=alex-ber-utils[tests]
```

Or explicitly:

```bash
wget https://github.com/alex-ber/scrapy-state/archive/master.zip -O master.zip; unzip master.zip; rm master.zip
```
And then installing from source (see below).


### Installing from source
```bash
python3 -m pip install . # only installs "required"
```
```bash
python3 -m pip install .[tests] # installs dependencies for tests
```

#### Alternatively you install install from requirements file:
```bash
python3 -m pip install -r requirements.txt # only installs "required"
```
```bash
python3 -m pip install -r requirements-tests.txt # installs dependencies for tests
```

##

From the directory with setup.py
```bash
python3 setup.py test #run all tests
```

or

```bash

pytest
```

## Installing new version
See https://docs.python.org/3.1/distutils/uploading.html 

```bash
python3 setup.py sdist upload
```

## Requirements


scrapy-state requires the following modules.

* Python 3.6+


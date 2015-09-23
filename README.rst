
Elastic Beanstalk Docker template for Django
============================================

Boilerplate Docker template for Django 1.8+ running Python 3.4.+ on AWS's Elastic Beanstalk

Elastic Beanstalk requires the following information to deploy an application:

* AWS access key ID
* AWS secret key
* Service region
* Application name
* Environment name
* Solution stack
* Git

Starting your project
=====================

Run the following command::

    $ django-admin.py startproject --template=https://github.com/glynjackson/django-docker-template/zipball/master mysite

Initialise your environment
===========================

If you have multiple AWS profiles already configured prefix this command with ``--profile YOURPROFILE``::

    ``eb init``

When prompted select the region from the list of given options then create/select an application name.
EB should detect your ``Dockerfile`` and ask "It appears you are using Docker. Is this correct?", answer yes.
It may ask you which platform version you are using, select ``Docker 1.6.2``.


Initialise and deploy the Django demo
=====================================

To setup the application in your newly created environment type::

    ``eb create``

The example Django application will take several minutes to deploy. Once deployed you can type ``eb open``.



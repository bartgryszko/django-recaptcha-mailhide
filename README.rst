reCAPTCHA Mailhide
==================

ReCAPTCHA Mailhide is an app for hiding mails from spammers. To use with
Django templates.

Installation
------------

Install using PIP

.. code:: sh

    pip install django-recaptcha-mailhide

Add “recaptcha-mailhide” to your INSTALLED\_APPS setting like this:

.. code:: python

    INSTALLED_APPS = (
        ...
        'recaptcha_mailhide',
    )

    MAILHIDE_PUBLIC_KEY = "XXX"
    MAILHIDE_PRIVATE_KEY = "XXX"

You can obtain public and private key for free via
http://www.google.com/recaptcha/mailhide/apikey

Usage
-----

First load it in Django template and use it as a filter.

.. code:: html+django

    {% load mailhide %}
    You can mail me at {{ "example@example"|mailhide }}

Credits
-------

Adapted from https://github.com/jbzdak/django-mailhide
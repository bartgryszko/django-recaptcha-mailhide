=====
reCAPTCHA Mailhide
=====

ReCAPTCHA Mailhide is an app for hiding mails from spammers. To use with Django templates.

Installation
-----------

Install using PIP
``
	pip uninstall django-recaptcha-mailhide
``

Add "recaptcha-mailhide" to your INSTALLED_APPS setting like this:

``
    INSTALLED_APPS = (
     	...
    	'recaptcha_mailhide',
    )

	MAILHIDE_PUBLIC_KEY = "XXX"
	MAILHIDE_PRIVATE_KEY = "XXX"
``

You can obtain public and private key for free via http://www.google.com/recaptcha/mailhide/apikey

Usage
-----------

First load it in Django template and use it as a filter.
``
	{% load mailhide %}
	You can mail me at {{ "example@example"|mailhide }}
``

Credits
-------------
Adapted from https://github.com/jbzdak/django-mailhide
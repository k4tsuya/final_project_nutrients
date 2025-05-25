# Commenting lines of code

Longer comments go over the line it is talking about, unless its a minor reminder, then it can go behind the code.

# Class structure

## Django-related classes

### Models

* field names should be kept brief and on the point
* boolean fields start with `is_`
* Order of sections is: Table fields, Meta class info, dunder methods (e.g. : `__str__` )

### Views and their associated HTML templates

* Don't forget to consider the request method (GET,POST, etc.)
* in the templates you can reference other templates in 2 ways:
  * Django Template:

    * [Example for User Registration and Login Authentication](https://youtu.be/tUqUdu0Sjyc "Goes over Registration, Login, Flash Messages, Warnings, Logging out and Restricting Login")
    * Avoid reusing the same name for various applications due to name clashing
    * DO NOT forget to link views from any views.py in a urls.py
    * if the link should do a query or find a specific like the year from an archive add `<type:name_of_argument>` to the reference
    * ```
      <a href="{% url 'login' %}">Login</a> will do a reverse search in your URLs to find a matching name
      ```
  * HTML: "/url_name/", this should lead to the direct path

    * ```
      <a href="/login/">Login</a> should get the user to website_url/login
      ```

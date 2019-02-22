# pnpl URL shrtnr

URL shortener micro service prototype based on Django Framework.

Django is a free, open source, high-end framework written in Python. It's also fast, flexible and got unit test framework, build in URL validator, form generator and ORM. So Django contains all the elements necessary for the realisation of such microservice from the box.

Pnpl Shrtnr may be used by itself as standalone application or be a part of other one. It consists from database with URLs and shortcodes for them, few functions (check submitted URL, isn't it already in db; generate shortcode for given URL; add new URL into db and assign generated shortcode to it; redirect to original URL from shortcode etc), few HTML pages to wrap it all in and this 'About' page.

Right now Pnpl Shrtnr fully covers the task - URL shortener micro service. But it can be easily improved by adding new features. Such as: URL usage stats; delete URL or make them inactive if they have been not used for a long time; create some Django commands for service management and maintaining; make service do something in situation when shortcode is incorrect or does not exist (now it shows Django 404 page); make another shortcode generator with words instead of letters and digits (pnpl.com/LazyNackedGekko) making links easy to remember or even give user a tool to make their own shortcodes.

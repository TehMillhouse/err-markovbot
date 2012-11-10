Err-MarkovBot
=============

Depenencies
-----------

This bot plugin relies on [PyMarkovChain](http://pypi.python.org/pypi/PyMarkovChain/) and the [Err Chatbot](http://gbin.github.com/err/)

Usage
-----

This plugin is pretty simple to use. Simply install it into your installation of [Err](http://gbin.github.com/err/), let it generate a database using one of the following:

```
!gendbfromfile <relative file path>
!gendbfromstring <string of characters>
!gendbfromurl <url>
```

Then use `!talk` or `!complete <text seed>` to make it speak. Enjoy!

Usage
=====

Basic Usage
-----------

.. code-block:: python

   from matrix_rain import YourClass
   
   obj = YourClass()
   result = obj.do_something()

Configuration
-------------

.. code-block:: python

   from matrix_rain.config import config
   
   config.set(debug=True, log_level="DEBUG")

Environment Variables
---------------------

* DEBUG - Enable debug mode (default: false)
* LOG_LEVEL - Set logging level (default: INFO)
* DATA_DIR - Directory for data files
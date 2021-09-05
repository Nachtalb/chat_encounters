Chat Encounters
============

A plugin for `Nicotine+`_.

Collect a record of who you talk with in case you accidentally close a chat tab.

Plugin created with `Nicotine+ Plugin Template`_ made by `Nachtalb`_.

Installation
------------

Open Nicotine+ settings, go to *General > Plugins* and click *+ Add
Plugins*. After that download the latest `release`_ and extract it into
the plugins folder.

Remove the version from the folder name. The folder name must stay the
same across version upgrades otherwise you will loose any changed
settings.

Now you can enable the *Chat Encounters* plugin in the previously
opened plugin settings.


Commands
--------

- ``/ce [who | how many]`` Show last encounters. By default the last 15. You can give another amount as argument or who.
- ``/ce-update`` manually check for updates.
- ``/ce-reload`` reload the plugin.


Settings
--------

+---------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Name                | Function                                                                                | Default                                                              |
+=====================+=========================================================================================+======================================================================+
| Check for Updates   | Check for updates on start and periodically                                             | Enabled                                                              |
+---------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+


Contributing
------------

Pull requests are welcome.


License
-------

`GNU GPL v3.0`_

.. _Nicotine+: https://nicotine-plus.github.io/nicotine-plus/
.. _Nicotine+ Plugin Template: https://github.com/Nachtalb/nicotine_plus_plugin_template
.. _Nachtalb: https://github.com/Nachtalb
.. _release: https://github.com/Nachtalb/chat_encounters/releases
.. _GNU GPL v3.0: https://github.com/Nachtalb/chat_encounters/blob/master/LICENSE

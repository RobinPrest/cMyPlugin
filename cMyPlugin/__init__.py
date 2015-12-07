# -*- coding: utf-8 -*-
"""
/***************************************************************************
 cMyPlugin
                                 A QGIS plugin
 Ce plugin est un test
                             -------------------
        begin                : 2015-12-07
        copyright            : (C) 2015 by Robin
        email                : a@b.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load cMyPlugin class from file cMyPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cMyPlugin import cMyPlugin
    return cMyPlugin(iface)

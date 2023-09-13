# -*- coding: utf-8 -*-
"""
/***************************************************************************
 convergence
                                 A QGIS plugin
 This plujgin allow to compute the layer of the CoE
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-09-12
        copyright            : (C) 2023 by Federico Gianoli
        email                : gianoli.federico@gmail.com
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

__author__ = 'Federico Gianoli'
__date__ = '2023-09-12'
__copyright__ = '(C) 2023 by Federico Gianoli'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load convergence class from file convergence.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CoE import convergencePlugin
    return convergencePlugin()
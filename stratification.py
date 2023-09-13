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
"""

__author__ = 'Federico Gianoli'
__date__ = '2023-09-12'
__copyright__ = '(C) 2023 by Federico Gianoli'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterRasterLayer
from qgis.core import QgsProcessingParameterFileDestination
from qgis.core import QgsProcessingParameterRasterDestination
import processing


class stratification(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer('raster_layer_with_classes', 'Raster Layer with classes', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterLayer('raster_layer_with_the_indicator', 'Raster Layer with the indicator', defaultValue=None))
        self.addParameter(QgsProcessingParameterFileDestination('MedianValues', 'Median values', optional=True, fileFilter='HTML files (*.html)', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Stratified', 'Stratified', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # stratification
        alg_params = {
            'LC': parameters['raster_layer_with_classes'],
            'issue': parameters['raster_layer_with_the_indicator'],
            'R_CONSOLE_OUTPUT': parameters['MedianValues'],
            'output': parameters['Stratified']
        }
        outputs['Stratification'] = processing.run('r:stratification', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['MedianValues'] = outputs['Stratification']['R_CONSOLE_OUTPUT']
        results['Stratified'] = outputs['Stratification']['output']
        return results

    def name(self):
        return 'stratification'

    def displayName(self):
        return 'stratification'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return stratification()

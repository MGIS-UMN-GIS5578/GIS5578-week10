# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Test-Toolbox"
        self.alias = "This is a blank tool template"

        # List of tool classes associated with this toolbox
        # self.tools must return a list
        # The object assigned to self.tools must match the object created 
        self.tools = [NewTool]


class NewTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Blank tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        # params = None
        params = arcpy.Parameter(displayName="Input Features", name="indataset", datatype="DEFeatureClass", parameterType="Required", direction="Input")
        return [params]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

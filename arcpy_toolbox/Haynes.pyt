import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "HaynesTest"
        self.alias = "Haynes"

        # List of tool classes associated with this toolbox
        #self.tools must return a list
        self.tools = [HaynesTool]


class HaynesTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "David Haynes Tool"
        self.description = "David Haynes arcpy tools"
        self.canRunInBackground = False
        #self.getParameterInfo()
        #arpy.Messages("Something")

    def getParameterInfo(self):
        """Define parameter definitions"""
        param1= arcpy.Parameter(displayName="Input Features", name="indataset", datatype="DEFeatureClass", parameterType="Required", direction="Input")

        #param1.filter.type ="Point"
        param2= arcpy.Parameter(displayName="Buffer Value", name="distance", datatype="GPLong", parameterType="Required", direction="Input")
        param4= arcpy.Parameter(displayName="Distance Measurement", name="unit", datatype="GPString", parameterType="Required", direction="Input")
        param3= arcpy.Parameter(displayName="Out Features", name="outdataset", datatype="DEFeatureClass", parameterType="Required", direction="Output")
        
        #param3= arcpy.Parameter(displayName="cities", name="toxic", datatype="Field", parameterType="Required", direction="Input")
        #param3.parameterDependencies = [param1.name]

        param4.filter.type = "Value List"
        param4.filter.list = ["Feet", "Meter"]

        #Must return a List object 
        #The order of the returned list affects the order of the boxes as they are displayed
        return[param1, param2, param4, param3 ]
        #return[param1,param4 ]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        # if parameters[2].altered:
        #     if parameters[2] in range(100): parameters[3].value = "NAME"
#arcpy.Describe(feature_class).shapeType
        if arcpy.Describe(parameters[0].value).shapeType != "Point":
            parameters[0].setErrorMessage("Only Point")

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        if parameters[1].value in range(100):
            arcpy.AddMessage("Value is good")
        else:
            parameters[1].setErrorMessage("Out of range")

        if arcpy.Describe(parameters[0].value).shapeType == "Point":
            arcpy.AddMessage("Ok")
        else:
            parameters[0].setErrorMessage("Only Point Feature Classes Allowed")

        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #arcpy.AddMessage(parameters)
        #boundary = paramaeters[0]
        inputFeatures = parameters[0].valueAsText 
        outputFeatures = parameters[3].valueAsText
        distance = parameters[1].valueAsText
        distance = "%s Feet" % (distance)
        
        #arcpy.AddMessage(inputFeatures)
        #arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, "FULL", "ROUND", "LIST")

        distance_with_unit = "%s %s" % (parameters[1].valueAsText, parameters[2].valueAsText)
        arcpy.AddMessage(distance_with_unit)
        arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance_with_unit, "FULL", "ROUND", "LIST")

        return

# -----------------
# My Geo Processing script
# Important lame information
# https://community.esri.com/thread/163291
# --------------------

import arcpy
import csv, os

def AddXYToShapefile(inFC, geomProperty, coordinateSystem):
    """
    http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-geometry-attributes.htm
    AddGeometryAttributes_management (Input_Features, Geometry_Properties, {Length_Unit}, {Area_Unit}, {Coordinate_System})
    """
    arcpy.AddGeometryAttributes_management(inFC, geomProperty, None, None, coordinateSystem)



def WriteShapeFileToCSV(aFeatureClass, fields, outCSV):
    """
    This function writes the shapefile/FeatureClass to the CSV provided.
   
    """
    import random

    fieldNames = [thefield.name for thefield in arcpy.ListFields(aFeatureClass)]
    
    matchedFields = [field for field in fields if field in fieldNames]
    #fieldNames = ["id", "INSIDE_X", "INSIDE_Y"]

    #Cycle through the dataset and write it out at the same time
    with arcpy.da.SearchCursor(aFeatureClass, matchedFields) as cursor, open(outCSV, 'w', newline="\n") as outFile:
        theWriter = csv.writer(outFile, delimiter=",")
        matchedFields.append("BUFFER")
        theWriter.writerow(matchedFields)
        
        for rec in cursor:
            #The rec object is a tuple, convert it to a list for CSV object
            outdata = [r for r in rec]
            #Adding randome value for buffer
            outdata.append(random.randrange(5,20))
            theWriter.writerow(outdata)


def CreateDataLayer(csvPath, xFieldName, yFieldName, layerName, coordinateSystem ):
    """
    http://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-xy-event-layer.htm
    arcpy.MakeXYEventLayer_management("firestations.dbf", "POINT_X", "POINT_Y", "firestations_points","", "POINT_Z")
    """

    layer = arcpy.MakeXYEventLayer_management(csvPath, xFieldName, yFieldName, layerName, coordinateSystem)

    return layer

def BufferPointLayer(inFC, outShapeFilePath, bufferDistance):
    """
    http://pro.arcgis.com/en/pro-app/tool-reference/analysis/buffer.htm
    arcpy.Buffer_analysis("roads", "C:/output/majorrdsBuffered", "100 Feet", "FULL", "ROUND", "LIST", "Distance")
    """

    arcpy.Buffer_analysis(inFC, outShapeFilePath, bufferDistance)



# ---------------- Program starts here --------------

#Set Input and output File names

myDirectory = r"C:\git\GIS5578_fall_2018\GIS5578-week10"
arcpy.env.workspace = myDirectory

polygonShapePath = os.path.join(myDirectory, "MSP_Communities_ACS.shp")
bufferShapePath = os.path.join(myDirectory, "buffer.shp")

pointLayerName = "cities"
pointCSVPath = os.path.join(myDirectory, '%s.csv'.format(pointLayerName,))
pointShapePath = os.path.join(myDirectory, '%s.shp'.format(pointLayerName,))

wgsCoordinateSystem = """GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"""
CSVFields = ["FID", "INSIDE_X", "INSIDE_Y"]



AddXYToShapefile(polygonShapePath, "CENTROID_INSIDE", wgsCoordinateSystem)
WriteShapeFileToCSV(polygonShapePath, CSVFields, pointCSVPath)
CreateDataLayer(pointCSVPath, CSVFields[1], CSVFields[2], pointLayerName, wgsCoordinateSystem )
#Copy Feature Layer to a shapefile
arcpy.CopyFeatures_management(pointLayerName, pointShapePath)
BufferPointLayer(pointShapePath, bufferShapePath, "BUFFER")
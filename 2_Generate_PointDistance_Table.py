import arcpy
import arcgisscripting,os
##arcpy.env.workspace = "C:/Users/Administrator/Documents/ArcGIS/Default.gdb"
##workspacePath= raw_input("Please Enter Workspace:")
workspacePath= R""
central_point=R""
ilist=os.listdir(workspacePath)
print "Table Start"
for shpFile in ilist:
    if shpFile[-4:]==".shp":
        #Change to 10
        arcpy.PointDistance_analysis(workspacePath+"/"+shpFile,central_point,"gdb location that you need to set such as:\\files.auckland.ac.nz\MyHome\Documents\ArcGIS\Zone\out_40000-40696_300m.gdb\C"+shpFile[:-4],"100 Meters")
print "Complete!"

import arcpy,os

workspacePath= R""#
cccc=R"//files.auckland.ac.nz/MyHome/Documents/ArcGIS/200.gdb/"#?????????
ilist=os.listdir(workspacePath)
name=r"H:\200.txt"
f  = open(name, "a+")
print "start"
for shpFile in ilist:
    if shpFile.endswith(".shp"):
        desc = arcpy.Describe("//files.auckland.ac.nz/MyHome/Documents/ArcGIS/200.gdb/C"+shpFile[:-4])
##        print desc.name
        prows = arcpy.SearchCursor(workspacePath + "/" + shpFile)
        ss=""
        for prow in prows:
            ss= str(desc.name[1:])+","+str(prow.getValue("ZONE")) +","+str(prow.getValue("ZONE_resol"))+","+str(prow.getValue("GROUPZONE"))+","+str(prow.getValue("GROUPZONE_"))+","+str(prow.getValue("SHAPE_Leng"))
        f.write(ss+'\n')
        rows = arcpy.SearchCursor(cccc+desc.name)
        str1=""
        for row in rows:
            str1=str(desc.name[1:])+","+str(row.getValue("NEAR_FID"))+","+str(row.getValue("DISTANCE"))
            f.write(str1+'\n')
f.close()
print "Finish!"

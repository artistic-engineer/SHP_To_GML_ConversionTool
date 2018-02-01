# Name: Divide Data based on Attributes
# Import system modules
import arcpy,arcgisscripting
from arcpy import env
# Set workspace
gp=arcgisscripting.create(10.1)
gp.workspace = r""
# Set local variables
in_features = "....shp"
#Confirm the out location
out_feature_class = R""
k=0
str1=''
cur=gp.SearchCursor(in_features)
##Define a blank dictionary
dict = {}
##Add value and key in blank dictionary
print "Data dividing..."
for rn in cur:
        str1=str(rn.FID)
        dict[rn.FID]=str1
##for key in dict:
##	print key,dict[key]
for key in dict:
    #Setting SQL clause
    where_clause = '"FID" = '+ ""+str(key)+ ""
##    print where_clause
#Implement the Select Analysis Function
    arcpy.Select_analysis(in_features, out_feature_class+"\\"+str(key)+".shp", where_clause)
print "Finish!"

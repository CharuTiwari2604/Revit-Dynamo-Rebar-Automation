import clr
clr.AddReference('RevitAPI')


from Autodesk.Revit.DB import *
from pyrevit import revit, forms

doc=revit.doc

cols=FilteredElementCollector(doc) \
.OfCategory(BuiltInCategory.OST_StructuralColumns) \
.WhereElementIsNotElementType() \
.ToElements()

total_vol=0.0

for c in cols:
    vol_param=c.LookupParameter('Volume')
    vol_ft=vol_param.AsDouble() if vol_param else 0.0
    total_vol+=(vol_ft*0.0283168)

msg= "{} Columns found. \nTotal Volume: {:.2f} m3".format(len(cols), total_vol)
forms.alert(msg, title="Structural Column Report")




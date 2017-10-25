import shapefile

w = shapefile.Writer()
w.shapeType = 1
print(w.shapeType)

# Add a point.
"""
w.field('name', 'testField1')
w.point(30.278042, -97.741049)
w.record('point1')
print(w)
# w.save('shapefiles/test/point')
"""

# Add a Polygon.
# """
w.field('name', 'testField2')
w.poly(parts=[[[122,37,4,9], [117,36,3,4]], [[115,32,8,8], [118,20,6,4], [113,24]]])
w.record('polygon1')
print(w)
w.save('shapefiles/test/polygon')
# """

# Add a Line.
"""
w.field('name', 'testField3')
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE)
w.record('line1')
w.record('line2')
print(w)
# w.save('shapefiles/test/line')
"""

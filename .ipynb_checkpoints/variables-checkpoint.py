import re

def TIF_APPLICATION_FLAT_QUERY():
    return "https://egis.baltimorecity.gov/egis/rest/services/Housing/TIF_Application_Data/MapServer/0/query?where=BVRI_FY26+%3D+%27Yes%27&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=FULLADDR%2C+BLOCKLOT%2C+Ownership%2C+Orig_Criteria%2C+Current_Criteria%2C+VRPA&returnGeometry=false&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=json"

def NEIGHBORHOOD_BOUNDARIES(name):
    location = re.sub(r"\s+", "+", name)
    print(location)
    return f"https://geodata.baltimorecity.gov/egis/rest/services/Housing/dmxFocusAreas/MapServer/2/query?where=Name='{location}'&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&f=json"
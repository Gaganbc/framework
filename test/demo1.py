from pyjavaproperties import Properties

# p=Properties()
# p.load(open('./../config.properties'))
# v=p["BROWSER"]
# print(v)
# v=p["ITO"]
# print(v)

def get_property(path,key):
    p = Properties()
    p.load(open(path))
    value=p[key]
    print('from property',key,value)
    return value

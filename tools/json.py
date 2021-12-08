import json
def printj(text): 
    tmpText = json.loads(text)
    tmpText1 = tmpText.dumps(tmpText,indent = 2)
    print(tmpText1)
json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'
printj(json_data)
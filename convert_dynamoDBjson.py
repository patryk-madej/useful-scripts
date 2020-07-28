#converts DynamoDB JSON into a list of lists
#turns N(number) records into integers, leaves everything else as a string

import json
def convert_dynamoDBjson(json):
    
    result=[]
    
    for i in range(len(json)):
        single_json=json[i]
        lst=[]

        for key in single_json.keys():
            temp_dict=single_json[key]

            for typ in temp_dict.keys():
                value=temp_dict[typ]
                if typ == 'N':
                    lst.append(int(value))
                else:
                    lst.append(value)

        result.append(lst)
    
    return result

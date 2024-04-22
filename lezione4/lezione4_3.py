def convert_to_title(cool_number:int)->str:
    while cool_number > 0:
        resto:int=(cool_number-1)%26
        result=chr(resto+ord("A"))+result
        cool_number=(cool_number-1)//26
    return result
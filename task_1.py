import json
def find_value(path):
    with open(path, encoding='utf-8') as file:
        data=json.load(file)
    # print(data)
    value=None
    while type(data)==dict or type(data)==list:
        if type(data)==dict:
            print('Available keys: ', data.keys())
            key=input()
            value=data[key]
            data=value
            continue
        if type(data)==list:
            print('Available indexes: ', len(data))
            index=int(input())
            value=data[index]
            data=value
    print(value)
if __name__=='__main__':
    find_value('/Users/vitalii/Desktop/Programming/2_semester/Lecture2/lab_2/twitter2.json')
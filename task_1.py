import json
def find_value(path):
    with open(path, encoding='utf-8') as file:
        data=json.load(file)
    store=[]
    store.append(data)
    while len(store)!=0:
        if type(store[-1])==dict:
            print('Available keys: ', store[-1].keys())
            key=input()
            if key=='.':            
                store.pop()                 
                continue
            store.append(store[-1][key])
            continue
        if type(store[-1])==list:
            print('Available indexes: ', len(store[-1]))
            index=input()
            if index=='.':
                store.pop()
                continue
            index=int(index)-1
            store.append(store[-1][index])
            continue
        print(store[-1])
        command=input()
        if command=='.':
            store.pop()
if __name__=='__main__':
    find_value('/Users/vitalii/Desktop/Programming/2_semester/Lecture2/lab_2/twitter2.json')